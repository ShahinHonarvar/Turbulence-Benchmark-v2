def return_vowels(s: str) -> list:
    vowels = []
    for char in s[149:313]:
        if 'M' < char <= 'j' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels