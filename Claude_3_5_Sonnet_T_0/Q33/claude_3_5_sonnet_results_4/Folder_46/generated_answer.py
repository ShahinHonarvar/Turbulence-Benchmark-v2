def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(10, 83):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and '%' < char <= 'e':
                result.append(string[i])
    return result