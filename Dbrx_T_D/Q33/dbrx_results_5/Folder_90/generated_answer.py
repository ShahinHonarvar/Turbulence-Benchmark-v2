def return_vowels(s: str) -> list:
    vowels = []
    for i in range(142, 145):
        if 4 < ord(s[i]) <= ord('o') and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels