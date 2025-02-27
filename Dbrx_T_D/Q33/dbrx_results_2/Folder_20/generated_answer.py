def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[59:61] if char in vowels and char > '+' and (char <= 'h')]