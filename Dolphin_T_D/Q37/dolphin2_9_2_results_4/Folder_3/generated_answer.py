def filter_chars(string):
    for i in range(37, 57):
        if '6' <= string[i] <= '_':
            string = string[:i] + string[i + 1:]
    return string