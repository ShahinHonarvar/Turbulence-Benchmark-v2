def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 55 or i >= 66 or (input_string[i] > 'f' and input_string[i] < '|'):
            filtered_string += input_string[i]
    return filtered_string