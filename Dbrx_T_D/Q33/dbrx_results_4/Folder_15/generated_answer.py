def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[5:7] if char > '3' and char <= '^' and (char in vowels)]
    return result