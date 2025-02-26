def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(24, 64):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'f' < char <= 'h':
                result.append(s[i])
    return result