def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(24, 64):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'F' < char <= 'h':
                result.append(char)
    return result