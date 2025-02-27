def filter_chars(string):
    for i in range(27, 75):
        if ord(string[i]) > ord('A') and ord(string[i]) < ord('i'):
            string = string.replace(string[i], '')
    return string