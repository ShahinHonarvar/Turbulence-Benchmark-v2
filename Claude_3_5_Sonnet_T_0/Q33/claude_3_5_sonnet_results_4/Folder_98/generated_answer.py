def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(3, 9):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 's' < char <= 'u':
                result.append(string[i])
    return result