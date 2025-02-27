def filter_chars(string):
    filtered_string = ''
    for i in range(46, 68):
        if string[i] > 'H' and string[i] < 's':
            filtered_string += string[i]
    return filtered_string