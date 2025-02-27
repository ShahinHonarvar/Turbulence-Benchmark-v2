def filter_chars(string):
    for i in range(722, 833):
        if string[i] >= 'K' and string[i] <= 'm':
            string = string.replace(string[i], '')
    return string