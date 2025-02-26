def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[71:81]:
        if char in vowels and '>' < char <= 'U':
            result.append(char)
    return result