def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(46, 49):
        if i < len(s) and s[i] > '[' and (s[i] <= 'p') and (s[i] in vowels):
            result.append(s[i])
    return result