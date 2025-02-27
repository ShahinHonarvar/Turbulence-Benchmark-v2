def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(37, 57):
        if s[i] > '*' and s[i] <= 'P' and (s[i] in vowels):
            result.append(s[i])
    return result