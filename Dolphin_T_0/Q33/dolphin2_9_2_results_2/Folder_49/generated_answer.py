def return_vowels(input_string):
    input_string = input_string[10:97]
    vowels = 'aeiou'
    result = []
    for char in input_string:
        if char > 'R' and char <= 'b':
            if char in vowels:
                result.append(char)
    return result