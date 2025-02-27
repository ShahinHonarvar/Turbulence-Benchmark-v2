def filter_chars(string):
    for char in set(string[259:503]):
        if ',' <= char <= '3':
            string = string.replace(char, '')
    return string