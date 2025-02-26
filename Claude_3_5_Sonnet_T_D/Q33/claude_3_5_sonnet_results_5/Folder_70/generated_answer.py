def return_vowels(input_string):
    vowels = 'aeiou'
    result = []
    for i in range(171, 402):
        if i < len(input_string):
            char = input_string[i].lower()
            if char in vowels and 'i' < char <= 'k':
                result.append(input_string[i])
    return result