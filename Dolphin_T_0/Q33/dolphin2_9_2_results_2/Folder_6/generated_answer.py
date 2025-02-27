def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(20, 34):
        if s[i] in vowels and s[i] > 'U' and (s[i] <= 'i'):
            result.append(s[i])
    return result