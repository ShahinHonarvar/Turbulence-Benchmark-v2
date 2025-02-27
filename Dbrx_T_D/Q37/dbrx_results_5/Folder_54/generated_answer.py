def filter_chars(input_string):
    start_index = 46
    end_index = 85
    ascii_range_start = ord('-')
    ascii_range_end = ord('X')
    for index in range(start_index, end_index + 1):
        if input_string[index] >= chr(ascii_range_start) and input_string[index] <= chr(ascii_range_end):
            input_string = input_string.replace(input_string[index], '', 1)
    return input_string