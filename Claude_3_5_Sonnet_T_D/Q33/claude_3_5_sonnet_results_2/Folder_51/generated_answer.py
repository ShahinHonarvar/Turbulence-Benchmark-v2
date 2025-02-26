def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[56:68]:
        if char in vowels and 'M' < char <= 'X':
            result.append(char)
    return result