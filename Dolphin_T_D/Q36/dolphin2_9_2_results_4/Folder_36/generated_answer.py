def filter_chars(string):
    for i in range(283, 484):
        if 'l' < string[i] < 't':
            string = string.replace(string[i], '')
    return string