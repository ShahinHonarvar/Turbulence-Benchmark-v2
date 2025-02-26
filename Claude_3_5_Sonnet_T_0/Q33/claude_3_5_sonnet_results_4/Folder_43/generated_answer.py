def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(22, 82):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'n' < char <= 'o':
                result.append(string[i])
    return result