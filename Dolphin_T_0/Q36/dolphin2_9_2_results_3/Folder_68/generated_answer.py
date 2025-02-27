def filter_chars(a_string):
    for i in range(1, 9):
        if '8' < a_string[i] < 'm':
            a_string = a_string.replace(a_string[i], '')
    return a_string