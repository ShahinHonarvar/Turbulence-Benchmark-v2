def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(24, 59):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'n' < char <= 'u':
                result.append(input_string[i])
    return result