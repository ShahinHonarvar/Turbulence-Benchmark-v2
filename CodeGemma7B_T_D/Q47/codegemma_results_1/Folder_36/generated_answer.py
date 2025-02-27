import re

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(115, 135):
            substring = text[max(0, i - j):i + j + 1]
            if len(substring) == j + 1 and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring.lower())
    return palindromes