def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(56, 68):
        if i < len(s) and s[i] > 'M' and (s[i] <= 'X') and (s[i] in vowels):
            result.append(s[i])
    return result