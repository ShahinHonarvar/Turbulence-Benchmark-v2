def filter_chars(input_str):
    char_list = list(input_str)
    for i in range(len(char_list)):
        if 24 < i < 37:
            if 'A' < char_list[i] < 'h':
                char_list[i] = ''
    return ''.join(char_list)