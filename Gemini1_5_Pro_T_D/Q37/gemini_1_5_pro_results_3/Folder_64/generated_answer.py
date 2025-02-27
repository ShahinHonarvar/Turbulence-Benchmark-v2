def filter_chars(string):
    for i in range(1, 8):
        if string[i] >= 'L' and string[i] <= 'a':
            string = string.replace(string[i], '')
    return string