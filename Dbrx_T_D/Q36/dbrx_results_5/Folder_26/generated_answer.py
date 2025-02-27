def filter_chars(input_string):
    for i in range(len(input_string)):
        if 43 < i < 83:
            if input_string[i] > ':' and input_string[i] < 'Q':
                input_string = input_string.replace(input_string[i], '', 1)
    return input_string