def return_vowels(s: str) -> list:
    vowels = []
    for i in range(23, 85):
        if 'w' < s[i] <= 'v' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels