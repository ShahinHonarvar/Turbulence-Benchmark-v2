def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(90, 97):
        if s[i] in vowels and '_' < s[i] <= 'x':
            result.append(s[i])
    return result