def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[24:64] if char.lower() in vowels and char > 'F' and (char <= 'h')]