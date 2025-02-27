def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(74, 96):
        if s[i] > 'I' and s[i] <= 'X' and (s[i] in vowels):
            result.append(s[i])
    return result