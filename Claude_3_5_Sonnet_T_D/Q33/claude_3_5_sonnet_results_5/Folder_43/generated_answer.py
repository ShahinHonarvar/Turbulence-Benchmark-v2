def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[22:82]:
        if char.lower() in vowels and 'N' < char <= 'o':
            result.append(char)
    return result