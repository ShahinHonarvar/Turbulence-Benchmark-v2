def filter_chars(input_string):
    start_index, end_index = (52, 81)
    ascii_range = range(ord('A'), ord('U') + 1)
    for i in range(start_index, end_index + 1):
        if ord(input_string[i]) in ascii_range:
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string