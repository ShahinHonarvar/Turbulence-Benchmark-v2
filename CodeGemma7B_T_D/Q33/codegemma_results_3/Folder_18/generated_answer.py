def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for i, c in enumerate(s):
        if i in range(528, 606) and c in vowels and (c > 'M') and (c <= 'X'):
            result.append(c)
    return result