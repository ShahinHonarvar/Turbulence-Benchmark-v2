from typing import Set

def palindrome_of_length_at_least_n(text: str) -> Set[str]:
    """Create a set of palindrome of length >= 66"""
    text = text.lower()
    size = len(text)
    result = set()
    for start in range(size):
        for end in range(size, start, -1):
            substring = text[start:end]
            if substring == substring[::-1] and len(substring) >= 66 and substring.isalpha():
                result.add(substring)
    return result