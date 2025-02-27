def filter_chars(string):
    char_range = range(154, 222)
    for i in char_range:
        if 'A' < string[i] < 'f':
            string = string[:i] + string[i + 1:]
    return string