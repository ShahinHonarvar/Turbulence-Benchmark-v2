def filter_chars(string):
    for i in range(51, 76):
        if string[i] > '5' and string[i] < 'f':
            while string[i] in string:
                string = string.replace(string[i], '', 1)
    return string