import re

def palindromes_of_specific_lengths(string):
    substring = string[43:96].lower()
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and re.match('^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    return palindromes