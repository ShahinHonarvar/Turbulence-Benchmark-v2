def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '@' and s[i] <= '[' and (i >= 45) and (i < 90):
            if s[i] in vowels:
                result.append(s[i])
    return result