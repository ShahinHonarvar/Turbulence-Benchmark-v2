from typing import Set, Optional

def palindrome_of_length_n(s: str) -> Set[str]:
    result = set()
    palindrome_length = 80
    for i in range(len(s) - palindrome_length + 1):
        substring = s[i:i + palindrome_length]
        if substring == substring[::-1]:
            result.add(substring)
    return result or None