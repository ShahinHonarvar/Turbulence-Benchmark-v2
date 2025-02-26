def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(44, 95):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and '5' < char <= '<':
                result.append(char)
    return result