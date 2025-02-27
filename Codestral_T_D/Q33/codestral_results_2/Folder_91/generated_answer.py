def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(4, 8):
        if s[i] in vowels and s[i] > 'P' and (s[i] <= 'r'):
            result.append(s[i])
    return result