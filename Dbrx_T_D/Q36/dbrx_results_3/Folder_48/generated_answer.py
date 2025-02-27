def filter_chars(input_string: str) -> str:
    start_index = 154
    end_index = 222
    char_set = set(range(ord('A'), ord('f') + 1))
    for char in char_set:
        input_string = input_string.replace(chr(char), '')
    return input_string[start_index:end_index]