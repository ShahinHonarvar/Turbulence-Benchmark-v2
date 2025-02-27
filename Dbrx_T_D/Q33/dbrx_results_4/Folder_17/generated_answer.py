def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[60:99] if c > 'j' and c <= 'n' and (c in vowels)]