def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(837, 975):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'n' < char <= 'w':
                result.append(s[i])
    return result