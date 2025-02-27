def filter_chars(input_string):
    start_index = 1
    end_index = 7
    for i in range(start_index, end_index):
        char = input_string[i]
        if '3' < char < '^':
            input_string = input_string.replace(char, '', 1)
    return input_string