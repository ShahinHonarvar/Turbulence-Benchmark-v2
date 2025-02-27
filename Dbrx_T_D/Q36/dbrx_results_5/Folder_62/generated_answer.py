def filter_chars(input_string):
    start_index = 63
    end_index = 89
    filtered_string = ''
    for i in range(len(input_string)):
        if i < start_index or i >= end_index:
            filtered_string += input_string[i]
        elif input_string[i] > '*' and input_string[i] < 'w':
            filtered_string += input_string[i]
        else:
            continue
    return filtered_string