def filter_chars(input_string):
    start_idx = 58
    end_idx = 81
    filtered_chars = []
    for i in range(len(input_string)):
        if i < start_idx or i >= end_idx:
            filtered_chars.append(input_string[i])
        elif input_string[i] > '5' and input_string[i] < '>':
            filtered_chars.append(input_string[i])
    return ''.join(filtered_chars)