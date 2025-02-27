import re

def palindromes_of_specific_lengths(text):
    text = text[11:97].lower()
    palindromes = set()
    for i in range(len(text) - 44):
        for j in range(i + 45, min(i + 53, len(text) + 1)):
            substring = text[i:j]
            if len(substring) >= 45 and len(substring) <= 52 and (substring == substring[::-1]) and re.match('^[a-z]+$', substring):
                palindromes.add(text[i:j])
    return palindromes