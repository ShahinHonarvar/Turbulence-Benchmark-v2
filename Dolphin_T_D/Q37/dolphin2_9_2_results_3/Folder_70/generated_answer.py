def filter_chars(string):
    for i in range(515, 539):
        if '+' <= string[i] <= '}':
            string = string.replace(string[i], '')
    return string