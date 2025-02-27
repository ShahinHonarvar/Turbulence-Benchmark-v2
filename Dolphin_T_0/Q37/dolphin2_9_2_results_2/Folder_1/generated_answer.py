def filter_chars(string):
    for i in range(41, 80):
        if 'f' <= string[i] <= '|':
            string = string[:i] + string[i + 1:]
    return string