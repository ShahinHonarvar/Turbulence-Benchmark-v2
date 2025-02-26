def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(14, 60):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'D' < char <= 'v':
                result.append(char)
    return result