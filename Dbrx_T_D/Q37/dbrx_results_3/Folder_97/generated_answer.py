def filter_chars(input_str):
    char_list = list(input_str)
    for i in range(len(char_list)):
        if i >= 227 and i <= 235:
            char = char_list[i]
            if 'D' <= char and char <= 'u':
                char_list[i] = ''
    return ''.join(char_list)