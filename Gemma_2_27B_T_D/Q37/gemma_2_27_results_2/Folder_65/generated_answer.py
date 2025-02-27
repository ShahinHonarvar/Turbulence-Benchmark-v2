def filter_chars(string):
    for i in range(61, 71):
        if i < len(string) and string[i] >= '0' and (string[i] <= '@'):
            string = string.replace(string[i], '')
    return string