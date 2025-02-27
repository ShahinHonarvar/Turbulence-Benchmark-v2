def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(149, 313):
        if s[i] in vowels and s[i] > 'M' and (s[i] <= 'j'):
            result.append(s[i])
    return result