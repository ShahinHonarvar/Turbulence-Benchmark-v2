import re

def palindromes_of_specific_lengths(s):
    substring = s[3:301]
    palindromes = set()
    for length in range(30, 301):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if re.match('^[a-zA-Z]*$', word) and word.lower() == word.lower()[::-1]:
                palindromes.add(word.lower())
    return palindromes