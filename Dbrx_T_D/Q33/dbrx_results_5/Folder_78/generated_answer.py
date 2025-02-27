def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[46:90] if char > '@' and char <= '[' and (char in vowels)]
    return result