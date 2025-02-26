def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[1:7]:
        if char.lower() in vowels and 'F' < char <= 'j':
            result.append(char)
    return result