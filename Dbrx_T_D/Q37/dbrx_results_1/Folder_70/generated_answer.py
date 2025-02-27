def filter_chars(input_string):
    char_list = list(input_string)
    for i in range(len(char_list)):
        if 515 <= i <= 538:
            char = char_list[i]
            if ord('+') <= ord(char) <= ord('}'):
                char_list[i] = ''
    return ''.join(char_list)