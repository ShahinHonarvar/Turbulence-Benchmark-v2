import re

def palindromes_between_indices(s: str) -> set:
    english_letters = re.compile('[a-zA-Z]')
    palindromes = set()
    for i in range(4, 10):
        substring = english_letters.findall(s[i:10])
        if len(substring) >= 7:
            palindromes.add(''.join(substring[::-1]) + ''.join(substring))
    return palindromes