def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(45, 76):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'b' < char <= 'z':
                result.append(string[i])
    return result