def return_vowels(s: str) -> list:
    vowels = [i for i in s[20:41] if i > 'K' and i <= 'Z' and (i in 'AEIOU')]
    return vowels