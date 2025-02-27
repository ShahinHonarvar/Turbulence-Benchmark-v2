def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[40:91] if char.lower() > 'a' and char.lower() <= 'x' and (char.lower() in vowels)]
    return result