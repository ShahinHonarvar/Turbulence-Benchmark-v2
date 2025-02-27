def filter_chars(string):
    for i in range(33, 84):
        if chr(i) > 'm' and chr(i) < 'w':
            string = string.replace(chr(i), '')
    return string