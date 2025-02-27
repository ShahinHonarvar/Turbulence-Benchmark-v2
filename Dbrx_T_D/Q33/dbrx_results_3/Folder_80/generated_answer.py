def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '/' and s[i] <= 'n' and (s[i] in vowels) and (i >= 85) and (i < 99):
            result.append(s[i])
    return result