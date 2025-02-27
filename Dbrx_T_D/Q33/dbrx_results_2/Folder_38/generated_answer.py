def return_vowels(s: str) -> list:
    vowels = [char for char in s[17:65] if 'U' < char <= '{' and char in 'AEIOUaeiou']
    return vowels