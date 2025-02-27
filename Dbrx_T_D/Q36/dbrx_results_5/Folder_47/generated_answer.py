def filter_chars(input_string):
    for i in range(45, 57):
        char = chr(i)
        if 'F' < char < 'n':
            input_string = input_string.replace(char, '', 1)
    return input_string