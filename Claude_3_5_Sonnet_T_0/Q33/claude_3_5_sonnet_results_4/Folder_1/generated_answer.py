def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(24, 64):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'f' < char <= 'h':
                result.append(string[i])
    return result