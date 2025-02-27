import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('\\W+', '', s.lower())
    return {s[i:j] for i in range(len(s)) for j in range(i + 74, len(s) + 1) if s[i:j] == s[i:j][::-1]}