def return_vowels(s: str) -> list:
    return [char for char in s[28:76] if 'a' <= char <= 'z' and char in 'aeiou']