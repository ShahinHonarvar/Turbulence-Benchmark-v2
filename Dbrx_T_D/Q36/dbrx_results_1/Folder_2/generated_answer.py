def filter_chars(input_string):
    start_index = 420
    end_index = 854
    for i in range(start_index, end_index):
        char = input_string[i]
        if 'D' < char < 'J':
            input_string = input_string.replace(char, '', 1)
    return input_string