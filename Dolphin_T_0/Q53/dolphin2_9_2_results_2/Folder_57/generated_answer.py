import re

def palindrome_of_length_at_least_n(s):
    set_palindromes = set()
    s = re.sub('[^A-Za-z]', '', s).lower()
    for i in range(len(s)):
        for j in range(i + 8, len(s) + 1):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 93:
                set_palindromes.add(substring)
    return set_palindromes