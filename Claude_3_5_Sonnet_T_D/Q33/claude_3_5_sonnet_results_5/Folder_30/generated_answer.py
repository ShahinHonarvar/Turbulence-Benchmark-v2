def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(11, 61):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'M' < char.upper() <= 'W':
                result.append(input_string[i])
    return result