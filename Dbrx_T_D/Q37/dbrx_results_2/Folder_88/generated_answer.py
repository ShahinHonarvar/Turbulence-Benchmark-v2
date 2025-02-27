def filter_chars(input_string):
    char_list = list(input_string)
    for index in range(69, 81):
        if char_list[index] >= '@' and char_list[index] <= 'p':
            char_list[index] = ''
    return ''.join(char_list)