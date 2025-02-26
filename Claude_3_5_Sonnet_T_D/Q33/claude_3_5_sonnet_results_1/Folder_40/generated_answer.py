def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[2:7]:
        if char in vowels and '^' < char <= 'd':
            result.append(char)
    return result