def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[1:4]:
        if char.lower() in vowels and 'C' < char <= 'I':
            result.append(char)
    return result