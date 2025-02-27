def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '<' and s[i] <= 'p' and (i >= 19) and (i < 20):
            if s[i] in vowels:
                result.append(s[i])
    return result