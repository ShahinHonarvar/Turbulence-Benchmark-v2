def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(len(char_list)):
        if 35 <= i <= 40 and ord(')') <= ord(char_list[i]) <= ord('l'):
            char_list[i] = ''
    return ''.join(char_list)