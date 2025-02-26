def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(56, 90):
        if i < len(string):
            char = string[i]
            if char.lower() in vowels and 'K' < char <= 'z':
                result.append(char)
    return result