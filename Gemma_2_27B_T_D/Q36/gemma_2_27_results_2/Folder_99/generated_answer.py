def filter_chars(string):
    for i in range(476, 948):
        if 'b' < string[i] < 'd':
            string = string.replace(string[i], '')
    return string