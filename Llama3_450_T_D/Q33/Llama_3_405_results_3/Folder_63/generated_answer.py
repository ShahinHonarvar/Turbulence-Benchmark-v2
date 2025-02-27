def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(34, 69):
        if i < len(s) and s[i] in vowels and ('_' < s[i] <= 'o'):
            result.append(s[i])
    return result