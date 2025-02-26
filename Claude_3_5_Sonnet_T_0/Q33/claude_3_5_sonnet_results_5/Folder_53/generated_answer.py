def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(27, 57):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'o' < char <= 'w':
                result.append(string[i])
    return result