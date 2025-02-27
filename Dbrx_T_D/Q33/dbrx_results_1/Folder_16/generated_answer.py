def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[133:306] if char > 'c' and char <= 'd' and (char in vowels)]