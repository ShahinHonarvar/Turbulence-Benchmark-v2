def filter_chars(input_str):
    start_index = 15
    end_index = 85
    char_list = list(input_str)
    for i in range(start_index, end_index):
        if 'I' < char_list[i] < 'M':
            char_list[i] = ''
    return ''.join(char_list)