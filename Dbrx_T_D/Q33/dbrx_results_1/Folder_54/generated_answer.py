def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if i >= 23 and i < 85 and (s[i] > 'W') and (s[i] <= 'v') and (s[i] in vowels):
            result.append(s[i])
    return result