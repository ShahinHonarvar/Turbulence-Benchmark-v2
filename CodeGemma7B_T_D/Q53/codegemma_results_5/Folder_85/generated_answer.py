from itertools import product
        import re

def palindrome_of_length_at_least_n(s: str) -> set[str]:
    s = s.lower()
    result = set()
    for i in range(0, len(s)):
        for j in range(i + 84, len(s) + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result