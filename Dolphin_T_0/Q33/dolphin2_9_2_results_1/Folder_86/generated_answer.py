def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(273, 275):
        if '+' < s[i] <= 'o':
            if s[i] in vowels:
                result.append(s[i])
    return result