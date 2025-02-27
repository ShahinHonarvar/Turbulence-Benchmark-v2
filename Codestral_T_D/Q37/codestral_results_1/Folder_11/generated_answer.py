def filter_chars(string):
    for char in sorted(set(string[29:98])):
        if '-' <= char <= 'n':
            string = string.replace(char, '')
    return string