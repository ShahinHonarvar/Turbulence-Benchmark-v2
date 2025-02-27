def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 35 or i > 98 or (input_string[i] < 'A' and input_string[i] > 'b'):
            filtered_string += input_string[i]
    return filtered_string