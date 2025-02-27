def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[41:50] if char > 'W' and char <= '[' and (char in vowels)]
    return result