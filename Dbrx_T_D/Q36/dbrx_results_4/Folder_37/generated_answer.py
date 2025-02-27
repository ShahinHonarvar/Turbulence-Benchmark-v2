def filter_chars(input_string):
    for i, char in enumerate(input_string):
        if 44 < i < 59 and '0' < char < '6':
            input_string = input_string.replace(char, '', 1)
    return input_string