def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[20:34]:
        if char.lower() in vowels and 'U' < char <= 'i':
            result.append(char)
    return result