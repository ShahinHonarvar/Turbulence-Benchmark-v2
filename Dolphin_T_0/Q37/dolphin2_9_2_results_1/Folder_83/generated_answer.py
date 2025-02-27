def filter_chars(string):
    for i in range(29, 80):
        if 'K' <= string[i] <= 'z':
            filtered_string = string.replace(string[i], '')
            return filtered_string
    return string