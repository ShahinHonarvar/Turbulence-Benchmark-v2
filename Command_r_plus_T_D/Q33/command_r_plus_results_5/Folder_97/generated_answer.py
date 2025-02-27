def return_vowels(s: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in s[328:455] if char in vowels and '>' in char <= 'z']