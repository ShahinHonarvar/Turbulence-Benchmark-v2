def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(55, 65):
        if s[i] > 'Z' and s[i] <= 'w':
            if s[i].lower() in vowels:
                result.append(s[i])
    return result