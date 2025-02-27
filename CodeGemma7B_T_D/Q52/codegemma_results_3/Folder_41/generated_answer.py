from typing import Set

def palindrome_of_length_n(s: str, n: int=60) -> Set[str]:
    seen = set()
    for start in range(len(s) - n + 1):
        word = s[start:start + n]
        seen.add(word.lower())
    return seen