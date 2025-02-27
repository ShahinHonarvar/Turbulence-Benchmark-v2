def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[1:5] if char > '!' and char <= 'j' and (char in vowels)]
    return result