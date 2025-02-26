def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(85, 99):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '/' < char <= 'n':
                result.append(string[i])
    return result