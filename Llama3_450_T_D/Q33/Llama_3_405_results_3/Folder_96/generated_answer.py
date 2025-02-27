def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(77, 84):
        if i < len(s) and s[i] in vowels and ('(' < s[i] <= 'G'):
            result.append(s[i])
    return result