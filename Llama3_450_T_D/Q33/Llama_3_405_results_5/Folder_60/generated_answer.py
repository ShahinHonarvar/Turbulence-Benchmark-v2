def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(24, 59):
        if i < len(s) and s[i] in vowels and ('N' < s[i] <= 'U'):
            result.append(s[i])
    return result