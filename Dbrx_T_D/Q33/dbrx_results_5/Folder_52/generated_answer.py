def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[24:68] if char > 'f' and char <= '|' and (char in vowels)]