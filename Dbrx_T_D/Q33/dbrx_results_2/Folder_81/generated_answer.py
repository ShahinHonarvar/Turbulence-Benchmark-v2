def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[20:43] if 5 < ord(char) <= ord('M') and char in vowels]