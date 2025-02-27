def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(36, 56):
        if i < len(s) and s[i] > '+' and (s[i] <= '/'):
            if s[i] in vowels:
                result.append(s[i])
    return result