def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(28, 76):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '+' < char <= 'z':
                result.append(char)
    return result