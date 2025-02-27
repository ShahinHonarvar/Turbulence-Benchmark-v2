import re

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(44, 100):
        for j in range(i + 13, min(i + 43, 100)):
            substring = text[i:j]
            if len(substring) >= 13 and len(substring) <= 42:
                if substring.lower() == substring[::-1].lower() and re.match('^[a-zA-Z]+$', substring):
                    palindromes.add(substring)
    return palindromes