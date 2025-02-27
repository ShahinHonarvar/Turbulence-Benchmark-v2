import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(max(0, i - 137), i + 1):
            palindrome_candidate = s[i - (i - j):i + 1]
            if palindrome_candidate == palindrome_candidate[::-1] and re.match('^[a-zA-Z]*$', palindrome_candidate):
                palindromes.add(palindrome_candidate.lower())
    return palindromes