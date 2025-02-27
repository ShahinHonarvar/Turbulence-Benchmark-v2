import re

def palindromes_of_specific_lengths(text: str) -> {str, set}:
    palindromes = set()
    for i in range(23, 83):
        for length in range(32, 35):
            substring = text[i:i + length]
            if substring and substring.lower() == substring.lower()[::-1] and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring)
    return palindromes