import re

def palindromes_of_specific_lengths(s):
    s = s[10:101].lower()
    return {palindrome for length in range(10, 51) for palindrome in {s[i:j] for i in range(len(s) - length + 1) for j in range(i + 1, i + length + 1) if s[i:j] == s[i:j][::-1]} if re.fullmatch('[a-z]*', palindrome)}