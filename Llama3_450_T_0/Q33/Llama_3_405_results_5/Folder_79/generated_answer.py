def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(74, 96):
        if i < len(s) and s[i] in vowels and ('I' < s[i] <= 'X'):
            result.append(s[i])
    return result