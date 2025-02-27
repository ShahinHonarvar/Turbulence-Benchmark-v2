def filter_chars(input_string):
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 348 or i > 852 or (input_string[i] < 'J' or input_string[i] > 'b'):
            filtered_string += input_string[i]
    return filtered_string