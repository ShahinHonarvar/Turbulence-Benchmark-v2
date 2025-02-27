def return_vowels(s: str) -> list:
    vowels = []
    for i in range(4, 8):
        if i >= len(s):
            break
        char = s[i]
        if 'P' < char <= 'r' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels