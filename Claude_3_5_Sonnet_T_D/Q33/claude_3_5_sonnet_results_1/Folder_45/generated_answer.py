def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for char in input_string[43:70]:
        if char in vowels and '*' < char <= 'b':
            result.append(char)
    return result