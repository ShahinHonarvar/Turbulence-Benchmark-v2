import re

def palindromes_of_specific_lengths(s):
    substr = s[30:96].lower()
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and re.match('^[a-zA-Z]*$', sub):
                palindromes.add(sub)
    return palindromes