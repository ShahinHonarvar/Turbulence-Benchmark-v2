def filter_chars(string):
    for i in range(155, 404):
        for c in string:
            if c == string[i]:
                string = string.replace(c, '', 1)
    return string