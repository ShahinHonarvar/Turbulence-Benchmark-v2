def filter_chars(string):
    for i in range(227, 236):
        if string[i] >= 'D' and string[i] <= 'u':
            string = string.replace(string[i], '')
    return string