def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(56, 96):
        if i < len(s) and s[i] in vowels and ('&' < s[i] <= 'T'):
            result.append(s[i])
    return result