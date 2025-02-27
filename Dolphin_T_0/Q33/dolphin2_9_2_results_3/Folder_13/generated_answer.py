def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(149, 313):
        if 'M' < s[i] <= 'j':
            if s[i] in vowels:
                result.append(s[i])
    return result