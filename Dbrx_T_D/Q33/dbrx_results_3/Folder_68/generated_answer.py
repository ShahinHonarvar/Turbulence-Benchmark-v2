def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[1:9] if 'b' < char <= 'k' and char in vowels]