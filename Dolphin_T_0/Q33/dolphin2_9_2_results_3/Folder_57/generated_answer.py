def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(21, 23):
        if s[i] > ' ' and s[i] <= 'n' and (s[i] in vowels):
            result.append(s[i])
    return result