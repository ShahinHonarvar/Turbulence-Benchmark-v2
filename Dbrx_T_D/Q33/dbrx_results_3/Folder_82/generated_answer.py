from typing import List

def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[86:99] if char in vowels and 'E' < char <= 'r']