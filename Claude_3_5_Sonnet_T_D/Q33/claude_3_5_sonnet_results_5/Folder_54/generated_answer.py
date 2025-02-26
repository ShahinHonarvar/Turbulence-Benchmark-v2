def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(23, 85):
        if i < len(input_string):
            char = input_string[i]
            if char.lower() in vowels and 'W' < char <= 'v':
                result.append(char)
    return result