def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = []
    for i in range(47, 61):
        if i < len(s) and s[i] in vowels and ('9' < s[i] <= 'O'):
            result.append(s[i])
    return result