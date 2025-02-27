def filter_chars(string):
    for i in range(33, 37):
        if ' ' < string[i] < 'A' and string[i] not in string[37:]:
            string = string.replace(string[i], '')
    return string