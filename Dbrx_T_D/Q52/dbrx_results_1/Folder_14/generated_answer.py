from typing import Set, Union

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def get_palindromes(n: int, string: str) -> Set[str]:
    if n % 2 == 0:
        return {substring for i in range(len(string) - n + 1) for substring in (string[i:i + n],) if is_palindrome(substring) and substring.isalpha()}

def palindrome_of_length_n(string: str, n: int=63) -> Set[str]:
    return get_palindromes(n, string.lower())