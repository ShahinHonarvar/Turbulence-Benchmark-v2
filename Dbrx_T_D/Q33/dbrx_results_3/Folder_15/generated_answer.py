def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(5, 6):
        if s[i] > '3' and s[i] <= '^' and (s[i] in vowels):
            result.append(s[i])
    return result