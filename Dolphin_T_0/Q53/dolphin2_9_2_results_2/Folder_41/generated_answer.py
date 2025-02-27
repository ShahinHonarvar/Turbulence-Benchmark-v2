import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(28, len(s) + 1):
        for i in range(len(s) - length + 1):
            s_temp = s[i:i + length]
            if s_temp == s_temp[::-1]:
                palindromes.add(s_temp)
    return palindromes