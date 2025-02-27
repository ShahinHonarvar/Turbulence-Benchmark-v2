def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(260, 322):
        if '!' <= s[i] <= 'U':
            if s[i] in vowels:
                result.append(s[i])
    return result