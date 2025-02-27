def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(86, 99):
        if i >= len(s) or s[i] < 'E' or s[i] > 'r':
            continue
        if s[i] in vowels:
            result.append(s[i])
    return result