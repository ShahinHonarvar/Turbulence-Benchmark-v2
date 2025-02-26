def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for i in range(528, 606):
        if i < len(string):
            char = string[i].upper()
            if char in vowels and 'M' < char <= 'X':
                result.append(string[i])
    return result