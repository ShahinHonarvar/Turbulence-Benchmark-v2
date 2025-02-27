def filter_chars(string):
    for i in range(27, 86):
        if 'c' <= string[i] <= 'i':
            string = string[:i] + string[i + 1:]
    return string