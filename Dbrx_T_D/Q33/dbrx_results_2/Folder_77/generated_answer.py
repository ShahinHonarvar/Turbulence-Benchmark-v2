def return_vowels(s: str) -> list[str]:
    vowels = []
    for i in range(837, 975):
        if len(s) > i and 'N' < s[i] <= 'W' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels