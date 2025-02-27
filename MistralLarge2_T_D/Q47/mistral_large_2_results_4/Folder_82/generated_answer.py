import re

def palindromes_of_specific_lengths(input_string):
    substring = input_string[3:301]
    palindromes = set()
    for length in range(30, 301):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate.lower())
    return palindromes