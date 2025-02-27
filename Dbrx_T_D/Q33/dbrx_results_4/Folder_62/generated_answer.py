def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(14, 60):
        if s[i] > 'D' and s[i] <= 'v' and (s[i] in vowels):
            result.append(s[i])
    return result