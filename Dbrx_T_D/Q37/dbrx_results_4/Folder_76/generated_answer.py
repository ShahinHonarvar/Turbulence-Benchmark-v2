def filter_chars(input_string):
    char_list = list(input_string)
    for i in range(len(char_list)):
        if i >= 379 and i <= 898 and ('M' <= char_list[i] <= 'v'):
            char_list[i] = ''
    return ''.join(char_list)