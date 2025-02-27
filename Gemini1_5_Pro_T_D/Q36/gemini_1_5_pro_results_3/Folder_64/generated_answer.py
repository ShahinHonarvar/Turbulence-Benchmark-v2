def filter_chars(string):
    for i in range(2, 6):
        if string[i] > '3' and string[i] < '^':
            string = string.replace(string[i], '')
    return string