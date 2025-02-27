def filter_chars(string):
    for i in range(58, 81):
        if string[i] > '5' and string[i] < '>':
            string = string.replace(string[i], '')
    return string