def return_vowels(s: str) -> list:
    vowels = []
    for char in s[41:50]:
        if 'W' < char <= '[' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels