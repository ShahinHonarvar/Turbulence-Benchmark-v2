import re
from typing import Set

def palindromes_between_indices(s: str) -> Set[str]:
    english_letters = re.findall('[a-zA-Z]', s[2:8])
    english_letters = [letter.lower() for letter in english_letters]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes