def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(483, 664):
        if s[i] > '&' and s[i] <= 'h' and (s[i] in vowels):
            result.append(s[i])
    return result