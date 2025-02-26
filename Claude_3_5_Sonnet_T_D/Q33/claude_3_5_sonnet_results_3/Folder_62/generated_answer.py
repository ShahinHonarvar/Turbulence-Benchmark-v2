def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(14, min(60, len(input_string))):
        if input_string[i] in vowels and 'D' < input_string[i] <= 'v':
            result.append(input_string[i])
    return result