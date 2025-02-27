def return_vowels(s: str) -> list:
    vowels = []
    for char in s[1:4]:
        if 'c' < char <= 'i' and char in 'aeiou':
            vowels.append(char)
    return vowels