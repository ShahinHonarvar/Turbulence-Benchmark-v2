import re

def palindromes_of_specific_lengths(text):
    text = text[70:141].lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 3, min(len(text) + 1, i + 61)):
            substring = text[i:j]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes