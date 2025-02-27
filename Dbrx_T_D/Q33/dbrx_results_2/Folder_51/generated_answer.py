def return_vowels(s: str) -> list[str]:
    vowels = []
    for i in range(len(s)):
        if i >= 56 and i < 68:
            if s[i] > 'M' and s[i] <= 'X' and (s[i] in 'AEIOUaeiou'):
                vowels.append(s[i])
    return vowels