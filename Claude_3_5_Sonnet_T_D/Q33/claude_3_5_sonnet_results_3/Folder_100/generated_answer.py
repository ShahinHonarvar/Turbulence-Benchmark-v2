def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 75):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'L' < char <= 'd':
                result.append(char)
    return result