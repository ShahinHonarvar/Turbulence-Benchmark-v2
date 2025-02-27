def filter_chars(string):
    for i in range(42, 68):
        if 't' < string[i] < 'x':
            string = string[:i] + string[i + 1:]
    return string