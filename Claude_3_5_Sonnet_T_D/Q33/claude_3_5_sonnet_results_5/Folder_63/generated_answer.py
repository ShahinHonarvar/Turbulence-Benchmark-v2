def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(34, 69):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and '_' < char <= 'o':
                result.append(char)
    return result