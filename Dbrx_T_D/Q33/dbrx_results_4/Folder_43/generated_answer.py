def return_vowels(s: str) -> list:
    return [c for c in s[22:82] if 'N' < c <= 'o' and c in 'aeiou']