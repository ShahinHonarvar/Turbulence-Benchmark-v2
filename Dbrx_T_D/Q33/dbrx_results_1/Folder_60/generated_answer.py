def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[24:59] if c > 'N' and c <= 'U' and (c in vowels)]