def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(2, 7):
        if i < len(s) and s[i] > '^' and (s[i] <= 'd') and (s[i] in vowels):
            result.append(s[i])
    return result