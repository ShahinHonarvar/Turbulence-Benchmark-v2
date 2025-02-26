def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[1:5]:
        if char.lower() in vowels and '!' < char <= 'j':
            result.append(char)
    return result