def filter_chars(input_string):
    char_list = list(input_string)
    for i in range(len(char_list)):
        if 41 <= i <= 64 and 'K' <= char_list[i] <= ']':
            char_list[i] = ''
    return ''.join(char_list)