def filter_chars(string):
    for i in range(283, 484):
        c = string[i]
        if c > 'l' and c < 't':
            string = string.replace(c, '')
    return string