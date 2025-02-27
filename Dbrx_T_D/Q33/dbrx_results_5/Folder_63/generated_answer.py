def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    result = []
    for i in range(34, 69):
        if i < len(s) and s[i] > '_' and (s[i] <= 'o') and (s[i] in vowels):
            result.append(s[i])
    return result