def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if i >= 604 and i < 949 and ('N' < s[i] <= 'U') and (s[i] in 'AEIOU'):
            vowels.append(s[i])
    return vowels