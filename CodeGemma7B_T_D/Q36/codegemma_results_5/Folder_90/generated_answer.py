def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 344 or i >= 874 or string[i] <= 'f' or (string[i] >= '~'):
            filtered_string += string[i]
    return filtered_string