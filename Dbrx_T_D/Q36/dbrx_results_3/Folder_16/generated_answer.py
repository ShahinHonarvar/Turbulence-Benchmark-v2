def filter_chars(input_string):
    start_index = 330
    end_index = 712
    for i in range(start_index, end_index):
        char = input_string[i]
        if 'M' < char < '_':
            input_string = input_string.replace(char, '', 1)
    return input_string