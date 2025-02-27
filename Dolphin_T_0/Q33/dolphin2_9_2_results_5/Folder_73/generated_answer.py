def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(47, 89):
        if i < len(s) and i >= 0 and (s[i] > '@') and (s[i] <= 'n'):
            if s[i] in vowels:
                result.append(s[i])
    return result