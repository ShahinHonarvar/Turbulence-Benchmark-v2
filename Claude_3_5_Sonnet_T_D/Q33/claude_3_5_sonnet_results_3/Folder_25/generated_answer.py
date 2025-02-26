def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(28, 76):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and '+' < char <= 'z':
                result.append(s[i])
    return result