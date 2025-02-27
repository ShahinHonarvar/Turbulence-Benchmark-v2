def filter_chars(string):
    for i in range(2, 7):
        if string[i] > '-' and string[i] < 'L':
            string = string.replace(string[i], '')
    return string