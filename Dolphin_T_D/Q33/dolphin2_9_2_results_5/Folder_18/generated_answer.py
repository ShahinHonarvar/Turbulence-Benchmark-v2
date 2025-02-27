def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(528, 606):
        if s[i] in vowels and s[i] > 'M' and (s[i] <= 'X'):
            result.append(s[i])
    return result