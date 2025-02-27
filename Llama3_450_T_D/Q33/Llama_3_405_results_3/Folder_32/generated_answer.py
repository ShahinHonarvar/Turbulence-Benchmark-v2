def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(45, 76):
        if i < len(s) and s[i].lower() in vowels and ('b' < s[i].lower() <= 'z'):
            result.append(s[i])
    return result