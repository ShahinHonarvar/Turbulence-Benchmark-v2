def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(5, 6):
        if 3 < ord(s[i]) <= ord('^') and s[i] in vowels:
            result.append(s[i])
    return result