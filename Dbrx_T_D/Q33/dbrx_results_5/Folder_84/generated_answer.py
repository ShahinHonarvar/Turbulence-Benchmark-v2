def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[770:852] if char > 'B' and char <= 'i' and (char in vowels)]