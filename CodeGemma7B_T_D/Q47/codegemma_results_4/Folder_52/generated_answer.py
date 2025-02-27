from typing import Set

def palindromes_of_specific_lengths(text: str) -> Set[str]:
    palindromes = set()
    for i in range(44, 100):
        for j in range(i + 13, i + 43):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes