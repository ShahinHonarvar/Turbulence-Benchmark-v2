def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(74, 96):
        if i < len(s):
            char = s[i].upper()
            if char in vowels and 'I' < char <= 'X':
                result.append(s[i])
    return result