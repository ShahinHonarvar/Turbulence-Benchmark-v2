import re
import string

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    s = re.sub(f'[^{re.escape(string.ascii_lowercase)}]', '', s)
    for i in range(len(s) - 67):
        for j in range(i + 68, len(s) + 1, 2):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes