def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(21, 59):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and '/' < char <= 'a':
                result.append(char)
    return result