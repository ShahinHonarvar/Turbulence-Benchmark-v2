import re

def palindromes_of_specific_lengths(s):
    s = s[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and re.match('^[A-Za-z]+$', sub):
                palindromes.add(sub.lower())
    return palindromes