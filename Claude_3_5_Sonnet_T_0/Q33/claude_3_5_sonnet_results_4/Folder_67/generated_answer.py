def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(21, 59):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '/' < char <= 'a':
                result.append(char)
    return result