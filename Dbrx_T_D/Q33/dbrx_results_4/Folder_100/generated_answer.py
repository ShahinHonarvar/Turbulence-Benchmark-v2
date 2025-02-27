def return_vowels(s: str) -> list:
    vowels = []
    for i in range(23, 75):
        if 'L' < s[i] <= 'd' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels