def return_vowels(s: str) -> list:
    return [char for char in s[11:61] if 'M' < char <= 'W' and char in 'AEIOU']