import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub(f'[^{re.escape(string.ascii_letters)}]', '', s)
    palindromes = set()
    for i in range(len(s) - 83):
        for j in range(i + 42, len(s) - 42):
            if s[i:j + 1] == s[i:j + 1][::-1] and len(s[i:j + 1]) >= 84:
                palindromes.add(s[i:j + 1])
    return palindromes