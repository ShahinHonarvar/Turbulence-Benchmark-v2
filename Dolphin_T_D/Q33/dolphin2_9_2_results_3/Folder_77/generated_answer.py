def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(837, 975):
        if i >= s.find('N') and i < s.find('W'):
            if s[i] in vowels:
                result.append(s[i])
    return result