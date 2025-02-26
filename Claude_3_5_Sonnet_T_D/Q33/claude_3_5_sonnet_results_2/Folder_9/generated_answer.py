def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[13:35]:
        if char in vowels and '8' < char <= 'F':
            result.append(char)
    return result