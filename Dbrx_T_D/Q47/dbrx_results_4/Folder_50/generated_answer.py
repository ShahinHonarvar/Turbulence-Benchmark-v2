import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(10, 36):
        for i in range(36, len(s) - length + 1):
            palindrome = s[i:i + length]
            if re.fullmatch('[a-z]*', palindrome) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes