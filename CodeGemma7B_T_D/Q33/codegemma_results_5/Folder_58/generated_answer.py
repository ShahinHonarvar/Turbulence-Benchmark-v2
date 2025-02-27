def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(260, 322):
        if input_string[i] in vowels and input_string[i] > '%' and (input_string[i] <= 'U'):
            result.append(input_string[i])
    return result