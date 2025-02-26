def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(27, 57):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'o' < char <= 'w':
                result.append(input_string[i])
    return result