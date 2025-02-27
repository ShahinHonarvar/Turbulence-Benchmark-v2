def filter_chars(input_string):
    for i in range(len(input_string)):
        if 77 < i < 87:
            if ';' < input_string[i] < 'r':
                input_string = input_string.replace(input_string[i], '', 1)
    return input_string