def filter_chars(input_string: str) -> str:
    char_list = list(input_string)
    for i in range(len(char_list)):
        if 38 <= i <= 54 and char_list[i] >= ':' and (char_list[i] <= 'r'):
            char_list[i] = ''
    return ''.join(char_list)