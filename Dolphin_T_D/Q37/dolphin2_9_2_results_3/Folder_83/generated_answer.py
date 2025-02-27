def filter_chars(string):
    for i in range(len(string)):
        if 29 <= i <= 79 and 'K' <= string[i] <= 'z':
            string = string[:i] + string[i + 1:]
    return string