def filter_chars(input_str):
    char_list = list(input_str)
    for i in range(len(char_list)):
        if 22 <= i <= 85:
            if '7' <= char_list[i] <= 'e':
                char_list[i] = ''
    return ''.join(char_list)