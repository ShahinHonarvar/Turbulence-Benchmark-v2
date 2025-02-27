from typing import Set

def palindrome_of_length_n(s: str) -> Set[str]:

    def is_palindrome(s):
        return s == s[::-1]
    n = 46
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            result.add(substring)
    return result