import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 72):
        for j in range(i + 36, len(s) - i + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all((char in string.ascii_letters for char in substring)):
                palindromes.add(substring)
    return palindromes