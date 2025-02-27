def filter_chars(string):
    for i in range(19, 33):
        if i < len(string) and string[i] >= 'f' and (string[i] <= 'o'):
            string = string.replace(string[i], '')
    return string