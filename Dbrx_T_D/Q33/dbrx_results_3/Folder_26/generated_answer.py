def return_vowels(s: str) -> list:
    vowels = []
    for i in range(10, 82):
        if s[i] > '$' and s[i] <= '@' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels