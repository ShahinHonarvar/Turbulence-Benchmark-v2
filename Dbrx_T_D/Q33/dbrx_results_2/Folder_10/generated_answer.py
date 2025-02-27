def return_vowels(s: str) -> list:
    vowels = []
    for i in range(31, 37):
        if s[i] > ';' and s[i] <= 't' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels