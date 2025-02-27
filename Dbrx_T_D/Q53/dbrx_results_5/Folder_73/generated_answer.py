import re
import string

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 94 + 1):
        for j in range(94, 0, -1):
            substring = s[i:i + j]
            if all((char in string.ascii_letters for char in substring)) and substring == substring[::-1] and (j >= 94):
                palindromes.add(substring)
    return palindromes