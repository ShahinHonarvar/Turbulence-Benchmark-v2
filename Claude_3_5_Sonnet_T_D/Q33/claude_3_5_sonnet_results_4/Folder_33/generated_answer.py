def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(163, 771):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and ':' < char <= 'E':
                result.append(char)
    return result