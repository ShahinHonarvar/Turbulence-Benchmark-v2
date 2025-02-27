def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 10 or i > 52 or (input_string[i] < '@' or input_string[i] > 'T'):
            result_string += input_string[i]
    return result_string