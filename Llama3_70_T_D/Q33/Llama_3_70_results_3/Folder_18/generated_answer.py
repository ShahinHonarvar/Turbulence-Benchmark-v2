def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(528, 606):
        if len(s) > i and s[i] in vowels and ('M' < s[i] <= 'X'):
            result.append(s[i])
    return result