def filter_chars(string):
    for i in range(54, 84):
        if 'j' <= string[i] <= 'v':
            string = string.replace(string[i], '')
    return string