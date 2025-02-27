def filter_chars(string):
    for i in range(35, 52):
        char = string[i].lower()
        if 'h' <= char <= 's':
            string = string.replace(string[i], '')
    return string