def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[60:99] if char > 'j' and char <= 'n' and (char in vowels)]