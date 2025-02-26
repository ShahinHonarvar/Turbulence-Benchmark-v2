def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, min(97, len(input_string))):
        if input_string[i] in vowels and 'R' < input_string[i] <= 'b':
            result.append(input_string[i])
    return result