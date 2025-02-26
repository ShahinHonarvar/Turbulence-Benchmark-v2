def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(45, 76):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'b' < char <= 'z':
                result.append(s[i])
    return result