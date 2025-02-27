import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.findall('[a-z]+', s)
    s = ''.join(s)
    n = 119
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1]}