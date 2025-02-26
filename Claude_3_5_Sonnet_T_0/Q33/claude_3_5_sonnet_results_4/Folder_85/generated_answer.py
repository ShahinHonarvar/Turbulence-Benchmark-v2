def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(55, 65):
        if i < len(string):
            char = string[i]
            if char.lower() in vowels and 'Z' < char <= 'w':
                result.append(char)
    return result