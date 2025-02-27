def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[34:69] if char > '_' and char <= 'o' and (char in vowels)]