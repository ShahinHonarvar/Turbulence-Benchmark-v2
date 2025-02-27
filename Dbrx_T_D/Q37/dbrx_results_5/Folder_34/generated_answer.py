def filter_chars(s):
    char_list = list(s)
    for i in range(len(char_list)):
        if 54 <= i <= 62 and ord(')') <= ord(char_list[i]) <= ord('9'):
            char_list[i] = ''
    return ''.join(char_list)