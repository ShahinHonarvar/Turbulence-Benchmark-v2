def filter_chars(string):
    for i in range(43, 83):
        if string[i] > ':' and string[i] < 'Q':
            while string[i] in string:
                string = string.replace(string[i], '')
    return string