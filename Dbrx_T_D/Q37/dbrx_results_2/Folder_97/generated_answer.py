def filter_chars(input_str):
    char_list = list(input_str)
    for i in range(len(char_list)):
        if i >= 227 and i <= 235:
            if char_list[i] >= 'D' and char_list[i] <= 'u':
                char_list[i] = ''
    return ''.join(char_list)