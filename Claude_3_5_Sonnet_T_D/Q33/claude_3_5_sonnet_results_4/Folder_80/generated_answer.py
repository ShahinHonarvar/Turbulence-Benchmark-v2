def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(85, 99):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and '/' < char <= 'n':
                result.append(input_string[i])
    return result