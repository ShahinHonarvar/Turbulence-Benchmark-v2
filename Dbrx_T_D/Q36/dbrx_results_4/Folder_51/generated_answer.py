def filter_chars(s):
    char_list = list(s)
    for i in range(len(char_list)):
        if 58 <= i < 81:
            if '5' < char_list[i] < '>':
                char_list[i] = ''
    return ''.join(char_list)