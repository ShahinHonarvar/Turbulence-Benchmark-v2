def filter_chars(string):
    """ Does what the user requested. """
    filtered_string = ''
    for i in range(len(string)):
        if i >= 8 and i <= 9 and (string[i] >= 'R') and (string[i] <= 't'):
            continue
        filtered_string += string[i]
    return filtered_string