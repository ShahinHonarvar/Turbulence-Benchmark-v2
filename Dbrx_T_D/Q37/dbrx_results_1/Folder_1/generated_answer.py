def filter_chars(input_string):
    filtered_list = []
    for i in range(len(input_string)):
        if i < 41 or i > 79 or input_string[i] < 'f' or (input_string[i] > '|'):
            filtered_list.append(input_string[i])
    return ''.join(filtered_list)