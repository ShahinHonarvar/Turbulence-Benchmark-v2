def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(273, 275):
        if i < len(s) and s[i] > '+' and (s[i] <= 'o') and (s[i] in vowels):
            result.append(s[i])
    return result