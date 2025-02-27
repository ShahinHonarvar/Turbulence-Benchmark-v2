def return_vowels(s: str) -> list:
    vowels = []
    for i in range(528, 606):
        if i < len(s) and 'M' < s[i] <= 'X' and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels