def filter_chars(string):
    for i in range(27, 86):
        for c in string:
            if string[i] == c:
                string = string.replace(c, '')
    return string