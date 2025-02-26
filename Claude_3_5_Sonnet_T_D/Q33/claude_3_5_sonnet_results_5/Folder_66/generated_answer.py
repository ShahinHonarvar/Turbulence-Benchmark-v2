def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[63:79]:
        if char in vowels and 'D' < char <= 'y':
            result.append(char)
    return result