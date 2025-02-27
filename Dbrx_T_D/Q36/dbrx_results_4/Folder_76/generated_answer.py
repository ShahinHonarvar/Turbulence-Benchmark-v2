def filter_chars(input_string):
    start_index = 668
    end_index = 888
    filtered_chars = []
    for i in range(len(input_string)):
        if i < start_index or i >= end_index:
            filtered_chars.append(input_string[i])
        elif input_string[i] > 'B' and input_string[i] < 'Y':
            filtered_chars.append(input_string[i])
    return ''.join(filtered_chars)