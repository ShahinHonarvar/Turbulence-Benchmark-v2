def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] > '/' and s[i] <= 'a' and (s[i] in vowels) and (i >= 21) and (i < 59):
            result.append(s[i])
    return result