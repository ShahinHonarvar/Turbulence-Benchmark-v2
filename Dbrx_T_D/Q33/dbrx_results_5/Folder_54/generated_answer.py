def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:85] if char > 'W' and char <= 'v' and (char in vowels)]