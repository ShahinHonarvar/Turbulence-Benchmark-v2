def return_vowels(s: str) -> list:
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = [char for char in s[40:91] if char in vowels and 'A' < char <= 'x']
    return result