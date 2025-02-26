def return_vowels(s):
    vowels = 'AEIOU'
    result = []
    for i in range(528, 606):
        if i < len(s):
            char = s[i].upper()
            if char in vowels and 'M' < char <= 'X':
                result.append(s[i])
    return result