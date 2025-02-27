def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[44:95] if char > '5' and char <= '<' and (char in vowels)]