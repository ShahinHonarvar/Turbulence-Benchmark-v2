def return_vowels(s: str) -> list:
    vowels = []
    for char in s[31:37]:
        if 'a' <= char <= 't' and char in 'aeiou':
            vowels.append(char)
    return vowels