import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 68):
        for j in range(i, len(s) - i + 1):
            if j - i + 1 >= 69:
                palindrome = s[i:j]
                if palindrome == palindrome[::-1] and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes