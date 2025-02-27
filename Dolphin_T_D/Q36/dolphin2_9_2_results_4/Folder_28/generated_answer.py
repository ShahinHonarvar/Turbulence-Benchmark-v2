def filter_chars(string):
    string = list(string)
    for i in range(31, 73):
        if 'M' < string[i] < 'j':
            while string[i] in string:
                string.remove(string[i])
    return ''.join(string)