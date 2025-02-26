def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(837, 975):
        if i < len(s):
            char = s[i].upper()
            if char in vowels and 'N' < char <= 'W':
                result.append(s[i])
    return result