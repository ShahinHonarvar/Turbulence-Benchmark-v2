def filter_chars(input_string):
    start_index = 2
    end_index = 7
    char_range = 'hi'
    for i in range(start_index, end_index):
        if input_string[i] > char_range[0] and input_string[i] < char_range[1]:
            input_string = input_string.replace(input_string[i], '', 1)
    return input_string