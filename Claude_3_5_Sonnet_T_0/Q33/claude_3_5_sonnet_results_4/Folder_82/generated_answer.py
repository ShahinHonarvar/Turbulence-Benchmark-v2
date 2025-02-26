def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(86, 99):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'e' < char <= 'r':
                result.append(string[i])
    return result