def filter_chars(string):
    filtered_string = ''
    for i in range(41, 87):
        if 'S' <= string[i] <= 's':
            string = string.replace(string[i], '')
    return string