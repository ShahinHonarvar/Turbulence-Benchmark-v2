def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= 'j' and s[i] <= 'n' and (i >= 60) and (i < 99) and (s[i] in vowels):
            result.append(s[i])
    return result