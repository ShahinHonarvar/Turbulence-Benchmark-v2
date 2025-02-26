def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 94):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '4' < char <= 'H':
                result.append(char)
    return result