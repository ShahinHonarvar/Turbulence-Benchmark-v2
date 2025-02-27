def filter_chars(input_string):
    filtered_string = ''
    for i in range(1, 7):
        char = input_string[i]
        if ord(',') < ord(char) < ord('f'):
            filtered_string = filtered_string.replace(char, '', 1)
    return filtered_string + input_string[7:]