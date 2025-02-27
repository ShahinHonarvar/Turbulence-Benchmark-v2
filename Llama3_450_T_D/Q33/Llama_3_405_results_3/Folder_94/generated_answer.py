def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(40, 94):
        if i < len(s) and s[i] in vowels and ('4' < s[i] <= 'H'):
            result.append(s[i])
    return result