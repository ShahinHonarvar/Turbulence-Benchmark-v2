import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('\\\\W+', '', s)
    n = 53
    return {s[i - n:i] for i in range(n, len(s) + 1) if s[i - n:i] == s[i - n:i][::-1]}