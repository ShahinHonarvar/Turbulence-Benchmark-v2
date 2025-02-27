def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[50:51] if char in vowels and 'a' < char <= 'v']