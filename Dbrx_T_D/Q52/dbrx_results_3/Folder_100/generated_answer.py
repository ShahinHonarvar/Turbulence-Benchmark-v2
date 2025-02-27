from typing import Set, Union

def is_palindrome(potential_palindrome: str) -> bool:
    return potential_palindrome.lower() == potential_palindrome[::-1].lower()

def get_letter_substrings(s: str) -> Set[str]:
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}

def palindrome_of_length_n(s: Union[str, None], n: int) -> Set[str]:
    if not s or n < 1 or len(s) < n:
        return set()
    letter_substrings = get_letter_substrings(s)
    return {sub_s for sub_s in letter_substrings if is_palindrome(sub_s) and len(sub_s) == n}