def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(22, 82):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'n' < char <= 'o':
                result.append(input_string[i])
    return result