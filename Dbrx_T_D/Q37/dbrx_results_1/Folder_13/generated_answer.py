def filter_chars(input_string):
    start_index = 124
    end_index = 854
    min_char = ord('9')
    max_char = ord('s')
    result_list = []
    for i, char in enumerate(input_string):
        if i < start_index or i > end_index:
            result_list.append(char)
        elif min_char <= ord(char) <= max_char:
            continue
        else:
            result_list.append(char)
    return ''.join(result_list)