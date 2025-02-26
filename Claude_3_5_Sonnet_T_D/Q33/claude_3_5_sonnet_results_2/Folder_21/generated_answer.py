def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(464, 574):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'a' < char <= 'g':
                result.append(char)
    return result