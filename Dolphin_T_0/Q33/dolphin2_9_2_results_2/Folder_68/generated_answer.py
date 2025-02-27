def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 9):
        if s[i] in vowels:
            if s[i] > '?' and s[i] <= 'k':
                result.append(s[i])
    return result