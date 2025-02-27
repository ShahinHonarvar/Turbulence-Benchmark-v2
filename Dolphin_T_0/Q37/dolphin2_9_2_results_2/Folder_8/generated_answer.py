def filter_chars(a_string):
    for i in range(41, 87):
        if a_string[i] >= 'S' and a_string[i] <= 's':
            a_string = a_string.replace(a_string[i], '')
    return a_string