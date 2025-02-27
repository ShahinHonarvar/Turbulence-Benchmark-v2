from typing import Set

def palindrome_of_length_at_least_n(s: str) -> Set[str]:
    """
    Returns the set of all palindromes of the length greater than or equal to 20 that exist in the given string.
    """
    palindrome = set()
    new_s = s.lower()
    for i in range(len(new_s)):
        for j in range(i + 20, len(new_s) + 1):
            lo = new_s[i:j]
            if lo == lo[::-1]:
                palindrome.add(s[i:j])
    return palindrome