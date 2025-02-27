def filter_chars(input_string):
    start_index = 219
    end_index = 403
    min_char = '*'
    max_char = '7'
    for i in range(len(input_string)):
        if input_string[i] > min_char and input_string[i] < max_char and (start_index < i < end_index):
            input_string = input_string.replace(input_string[i], '')
    return input_string