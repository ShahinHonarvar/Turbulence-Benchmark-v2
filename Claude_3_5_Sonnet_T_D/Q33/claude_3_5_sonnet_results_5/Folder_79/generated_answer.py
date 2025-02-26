def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for i in range(74, 96):
        if i < len(string):
            char = string[i].upper()
            if char in vowels and 'I' < char <= 'X':
                result.append(string[i])
    return result