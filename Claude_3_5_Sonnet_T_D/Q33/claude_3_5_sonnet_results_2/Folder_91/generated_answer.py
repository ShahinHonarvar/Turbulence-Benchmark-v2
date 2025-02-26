def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for char in input_string[4:8]:
        if char.lower() in vowels and 'P' < char <= 'r':
            result.append(char)
    return result