def return_vowels(s: str) -> list:
    vowels = []
    for char in s[1:9]:
        if 'a' <= char <= 'k' and char in 'aeiou':
            vowels.append(char)
    return vowels