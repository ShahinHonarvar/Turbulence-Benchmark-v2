from typing import Set

def palindrome_of_length_n(text: str) -> Set[str]:
    palindromes = set()
    for i in range(len(text) - 16):
        substring = text[i:i + 17].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes