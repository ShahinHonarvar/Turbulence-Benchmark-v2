def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 91):
        if s[i] in vowels:
            result.append(s[i])
    return result