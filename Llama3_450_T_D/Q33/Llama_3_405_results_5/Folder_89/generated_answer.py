def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(50, 51):
        if i < len(s) and s[i] > ',' and (s[i] <= 'v') and (s[i] in vowels):
            result.append(s[i])
    return result