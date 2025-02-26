def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(60, 99):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'j' < char <= 'n':
                result.append(string[i])
    return result