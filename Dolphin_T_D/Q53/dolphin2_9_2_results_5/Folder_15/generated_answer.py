import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    return set(filter(lambda p: len(p) >= 4, set((s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)) if s[i:j + 1] == s[j:i - 1:-1]))))