def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(133, 306):
        if s[i] > 'c' and s[i] <= 'd' and (s[i] in vowels):
            result.append(s[i])
    return result