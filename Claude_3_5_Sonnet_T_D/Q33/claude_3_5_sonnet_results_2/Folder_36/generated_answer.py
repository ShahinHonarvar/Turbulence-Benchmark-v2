def return_vowels(input_string):
    vowels = 'AEIOU'
    result = []
    for i in range(604, 949):
        if i < len(input_string):
            char = input_string[i].upper()
            if char in vowels and 'N' < char <= 'U':
                result.append(input_string[i])
    return result