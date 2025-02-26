def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 85):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'W' < char <= 'v':
                result.append(char)
    return result