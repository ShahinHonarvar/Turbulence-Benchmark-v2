def filter_chars(string):
    for i in range(18, 95):
        if string[i] > 'K' and string[i] < 'a':
            string = string.replace(string[i], '')
    return string