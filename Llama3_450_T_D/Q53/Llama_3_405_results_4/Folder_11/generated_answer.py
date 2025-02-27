import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    return set((i for i in (s[x:y] for x in range(len(s)) for y in range(x + 54, len(s) + 1)) if i == i[::-1]))