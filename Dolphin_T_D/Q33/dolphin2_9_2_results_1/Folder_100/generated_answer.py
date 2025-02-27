def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 75):
        if 'L' < s[i] <= 'd':
            if s[i] in vowels:
                result.append(s[i])
    return result