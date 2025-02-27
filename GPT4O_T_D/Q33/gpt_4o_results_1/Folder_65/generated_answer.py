def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    result = []
    for char in input_string[71:88]:
        if char in vowels and '9' < char <= 'P':
            result.append(char)
    return result