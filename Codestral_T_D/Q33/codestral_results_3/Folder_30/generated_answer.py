def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(11, 61):
        if s[i] in vowels and s[i] > 'M' and (s[i] <= 'W'):
            result.append(s[i])
    return result