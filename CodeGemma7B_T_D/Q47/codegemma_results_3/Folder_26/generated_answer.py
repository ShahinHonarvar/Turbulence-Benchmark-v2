import re

def palindromes_of_specific_lengths(s):
    pattern = re.compile('[a-zA-Z]{21,31}')
    palindromes = set()
    for i in range(24, 85):
        for j in range(i + 20, i + 32):
            word = s[i:j + 1]
            if pattern.fullmatch(word):
                palindromes.add(word)
    return palindromes