import re

def palindromes_of_specific_lengths(string):
    substring = string[:6].lower()
    lengths = range(3, 6)
    patterns = [''.join(reversed(pattern)) for pattern in map(str, lengths)]
    palindrome_set = set()
    for pattern in patterns:
        for start in range(len(substring) - pattern + 1):
            word = substring[start:start + int(pattern)]
            if word == pattern:
                palindrome_set.add(word)
    return palindrome_set