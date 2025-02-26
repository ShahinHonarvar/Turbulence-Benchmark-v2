def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(86, 99):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'E' < char <= 'r':
                result.append(char)
    return result