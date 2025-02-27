import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75].lower()
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            subsequence = substring[i:i + length]
            if subsequence == subsequence[::-1] and re.match('^[a-zA-Z]*$', subsequence):
                palindromes.add(subsequence)
    return palindromes