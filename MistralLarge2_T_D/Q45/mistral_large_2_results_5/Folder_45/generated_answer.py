import re

def palindromes_between_indices(s):
    substr = ''.join(re.findall('[a-zA-Z]', s[5:10])).lower()
    palindromes = set()
    for length in range(4, len(substr) + 1):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes