def return_vowels(s: str) -> list:
    vowels = []
    for char in s[56:96]:
        if 'a' <= char <= 'T' and char in 'aeiou':
            vowels.append(char)
    return vowels