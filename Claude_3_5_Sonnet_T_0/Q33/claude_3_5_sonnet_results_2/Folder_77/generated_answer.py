def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(837, 975):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'n' < char <= 'w':
                result.append(string[i])
    return result