def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(273, 275):
        if i < len(s) and s[i] in vowels and ('+' < s[i] <= 'o'):
            result.append(s[i])
    return result