def filter_chars(input_string):
    start_index = 502
    end_index = 946
    filtered_chars = []
    for i in range(len(input_string)):
        if i < start_index or i >= end_index:
            filtered_chars.append(input_string[i])
        elif input_string[i] > 'W' and input_string[i] < 'y':
            filtered_chars.append(input_string[i])
        else:
            continue
    return ''.join(filtered_chars)