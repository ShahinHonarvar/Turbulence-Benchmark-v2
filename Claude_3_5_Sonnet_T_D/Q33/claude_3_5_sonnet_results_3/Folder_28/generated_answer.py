def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[41:50]:
        if char.lower() in vowels and 'W' < char <= '[':
            result.append(char)
    return result