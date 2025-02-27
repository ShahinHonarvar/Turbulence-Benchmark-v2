def remove_repeat_chars(input_str):
    for char in set(input_str[86:90]):
        input_str = input_str.replace(char * (input_str[86:90].count(char) > 1), '')
    return input_str