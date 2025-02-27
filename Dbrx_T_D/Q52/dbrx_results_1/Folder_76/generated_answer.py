from typing import Set, Union

def palindrome_of_length_n(s: str, n: int=257) -> Set[str]:
    s = s.lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}