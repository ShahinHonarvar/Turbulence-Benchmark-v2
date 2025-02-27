import re

def palindromes_between_indices(s):
    palindromes = set()
    substr = s[0:7].lower()
    for i in range(len(substr) - 5):
        for j in range(i, len(substr) - 1):
            candidate = substr[i:j + 1]
            if candidate == candidate[::-1] and re.match('^[a-zA-Z]*$', candidate):
                palindromes.add(candidate)
    return palindromes