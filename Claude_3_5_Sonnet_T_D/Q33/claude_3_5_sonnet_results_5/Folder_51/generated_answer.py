def return_vowels(input_string):
    vowels = 'AEIOU'
    result = []
    for i in range(56, 68):
        if i < len(input_string):
            char = input_string[i].upper()
            if char in vowels and 'M' < char <= 'X':
                result.append(char)
    return result