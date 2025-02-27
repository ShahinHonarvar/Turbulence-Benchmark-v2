def filter_chars(string):
    for i in range(259, 503):
        if ',' <= string[i] <= '3':
            string = string.replace(string[i], '')
    return string