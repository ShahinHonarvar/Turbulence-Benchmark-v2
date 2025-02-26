def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(3, min(9, len(input_string))):
        char = input_string[i].lower()
        if char in vowels and 's' < char <= 'u':
            result.append(input_string[i])
    return result