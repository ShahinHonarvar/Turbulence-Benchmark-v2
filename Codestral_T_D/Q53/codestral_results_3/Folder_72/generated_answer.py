import re

def palindrome_of_length_at_least_n(string):
    substrings = [string[i:j] for i in range(len(string)) for j in range(i + 88, len(string) + 1)]
    substrings = [s for s in substrings if re.match('^[a-zA-Z]*$', s)]
    palindromes = [s for s in substrings if s.lower() == s.lower()[::-1]]
    return set(palindromes)