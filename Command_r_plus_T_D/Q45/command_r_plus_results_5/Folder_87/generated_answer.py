import re
from itertools import permutations

def palindromes_between_indices(s: str) -> set:
    english_letters = re.findall('[a-zA-Z]', s[3:10])
    palindromes = set()
    for perm in permutations(english_letters, len(english_letters)):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes