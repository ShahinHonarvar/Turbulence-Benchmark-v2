def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(59, 61):
        if s[i] in vowels and '+' < s[i] <= 'h':
            result.append(s[i])
    return result