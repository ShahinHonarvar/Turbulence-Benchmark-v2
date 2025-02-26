def return_vowels(string):
    vowels = 'aeiou'
    result = []
    for i in range(604, 949):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'n' < char <= 'u':
                result.append(string[i])
    return result