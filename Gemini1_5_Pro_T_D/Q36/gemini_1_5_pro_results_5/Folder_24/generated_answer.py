def filter_chars(string):
    for i in range(10, 15):
        if i >= len(string):
            break
        if 't' < string[i] < 'v':
            string = string.replace(string[i], '')
    return string