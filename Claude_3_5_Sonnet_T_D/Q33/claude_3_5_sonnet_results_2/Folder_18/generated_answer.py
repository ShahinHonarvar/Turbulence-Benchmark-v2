def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(528, 606):
        if i < len(input_string):
            char = input_string[i]
            if char in vowels and 'M' < char <= 'X':
                result.append(char)
    return result