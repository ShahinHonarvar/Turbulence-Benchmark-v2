def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] > '+' and s[i] <= 'W' and (i >= 11) and (i < 53):
            if s[i] in vowels:
                result.append(s[i])
    return result