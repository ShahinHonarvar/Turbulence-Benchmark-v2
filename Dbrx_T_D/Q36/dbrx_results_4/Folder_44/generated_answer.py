def filter_chars(string_arg):
    char_list = list(string_arg)
    for i in range(18, 64):
        if char_list[i] > '3' and char_list[i] < 'B':
            char_list[i] = None
    return ''.join(filter(None, char_list))