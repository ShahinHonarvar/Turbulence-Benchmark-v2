def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(142, 145):
        if i < len(s) and s[i] > '4' and (s[i] <= 'o') and (s[i] in vowels):
            result.append(s[i])
    return result