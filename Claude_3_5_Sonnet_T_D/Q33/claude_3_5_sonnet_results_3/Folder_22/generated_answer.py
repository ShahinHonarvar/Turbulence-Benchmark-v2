def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[56:90]:
        if char in vowels and 'K' < char <= 'z':
            result.append(char)
    return result