def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 57):
        if i < len(s) and s[i] >= '0' and (s[i] <= 'd') and (s[i] in vowels):
            result.append(s[i])
    return result