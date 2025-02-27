def return_vowels(s: str) -> list:
    vowels = []
    for i in range(len(s)):
        if i >= 11 and i < 53:
            if s[i] > '+' and s[i] <= 'W' and (s[i] in 'AEIOUaeiou'):
                vowels.append(s[i])
    return vowels