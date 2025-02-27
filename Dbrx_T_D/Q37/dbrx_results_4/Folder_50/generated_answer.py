def filter_chars(input_string):
    start_index = 71
    end_index = 96
    char_range_start = '_'
    char_range_end = 'o'
    for i in range(len(input_string)):
        if start_index <= i <= end_index and char_range_start <= input_string[i] <= char_range_end:
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string