def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for i in range(483, 664):
        if s[i] > '&' and s[i] <= 'h':
            if s[i] in vowels:
                result.append(s[i])
    return result