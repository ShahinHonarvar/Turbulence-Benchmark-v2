def filter_chars(string):
    r = ''
    for i in range(len(string)):
        if i >= 19 and i <= 22:
            if not (string[i] >= ']' and string[i] <= 't'):
                r += string[i]
        else:
            r += string[i]
    return r