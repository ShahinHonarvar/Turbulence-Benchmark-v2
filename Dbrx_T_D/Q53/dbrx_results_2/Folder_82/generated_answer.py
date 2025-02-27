import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    return {palindrome for i in range(len(s)) for palindrome in (s[i:i + n] for n in range(72, len(s) - i + 1) if s[i:i + n] == s[i:i + n][::-1])}