def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[47:89] if char > '@' and char <= 'n' and (char in vowels)]