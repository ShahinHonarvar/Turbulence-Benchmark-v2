def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(528, 606):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'M' < input_string[i] <= 'X':
                result.append(input_string[i])
    return result