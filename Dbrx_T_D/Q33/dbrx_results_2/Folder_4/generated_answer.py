def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[40:91] if char > 'A' and char <= 'x' and (char in vowels)]
    return result