def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 72 or i >= 93 or (input_string[i] > '<' and input_string[i] < 'J'):
            result_string += input_string[i]
    return result_string