def filter_chars(string):
    for i in range(19, 38):
        c = string[i]
        if ')' < c < 'P':
            string = string.replace(c, '')
    return string