def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if s[i] > 'N' and s[i] <= 'W' and (s[i] in vowels):
            result.append(s[i])
    return result