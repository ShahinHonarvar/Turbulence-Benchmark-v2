def filter_chars(string):
    for i in range(14, 75):
        if '9' < string[i] < 'K':
            string = string.replace(string[i], '')
    return string