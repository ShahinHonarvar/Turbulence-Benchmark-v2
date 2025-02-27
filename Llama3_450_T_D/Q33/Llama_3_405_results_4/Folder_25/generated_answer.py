def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(28, 76):
        if i < len(s) and s[i] > '+' and (s[i] <= 'z') and (s[i] in vowels):
            result.append(s[i])
    return result