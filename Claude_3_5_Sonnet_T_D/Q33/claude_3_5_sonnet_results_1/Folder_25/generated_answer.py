def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(28, 76):
        if i < len(s):
            if s[i].lower() in vowels and '+' < s[i] <= 'z':
                result.append(s[i])
    return result