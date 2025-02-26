def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(4, 8):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'p' < char <= 'r':
                result.append(string[i])
    return result