def filter_chars(input_string):
    result_string = ''
    for i in range(len(input_string)):
        if i < 36 or i > 79:
            result_string += input_string[i]
        elif input_string[i] < '2' or input_string[i] > 's':
            result_string += input_string[i]
    return result_string