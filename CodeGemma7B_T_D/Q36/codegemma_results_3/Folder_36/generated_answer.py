def filter_chars(string):
    for i in range(283, 485):
        if string[i] > 'l' and string[i] < 't':
            string = string.replace(string[i], '')
    return string