def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(202, 872):
        if s[i] > '3' and s[i] <= '>':
            if s[i] in vowels:
                result.append(s[i])
    return result