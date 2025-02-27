def filter_chars(input_string: str) -> str:
    start_index = 46
    end_index = 74
    for i in range(start_index, end_index):
        char = input_string[i]
        if ord(char) > ord('&') and ord(char) < ord('M'):
            input_string = input_string.replace(char, '', 1)
    return input_string