def filter_chars(input_string):
    start_index = 225
    end_index = 381
    lower_limit = ord('D')
    upper_limit = ord('Y')
    filtered_chars = []
    for i in range(len(input_string)):
        if i < start_index or i > end_index:
            filtered_chars.append(input_string[i])
        elif input_string[i] >= lower_limit and input_string[i] <= upper_limit:
            continue
        else:
            filtered_chars.append(input_string[i])
    return ''.join(filtered_chars)