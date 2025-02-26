def return_vowels(input_string):
    vowels = 'AEIOU'
    result = []
    for char in input_string[11:61]:
        if char.upper() in vowels and 'M' < char.upper() <= 'W':
            result.append(char)
    return result