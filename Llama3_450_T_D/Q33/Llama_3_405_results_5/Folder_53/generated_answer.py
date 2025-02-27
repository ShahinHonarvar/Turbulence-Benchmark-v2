def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(27, 57):
        if i < len(s) and s[i] > 'o' and (s[i] <= 'w') and (s[i] in vowels):
            result.append(s[i])
    return result