def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= 'N' and s[i] <= 'o' and (i >= 22) and (i < 82):
            if s[i] in vowels:
                result.append(s[i])
    return result