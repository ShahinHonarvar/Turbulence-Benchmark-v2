def return_vowels(s: str) -> list:
    vowels = []
    for i in range(149, 313):
        if s[i] > 'M' and s[i] <= 'j' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels