def filter_chars(input_str: str) -> str:
    start_index = 23
    end_index = 83
    char_range = range(ord('f') + 1, ord('o'))
    for i in char_range:
        if input_str[start_index:end_index].count(chr(i)) > 0:
            input_str = input_str.replace(chr(i), '', input_str[start_index:end_index].count(chr(i)))
    return input_str