def filter_chars(string):
    for i in range(48, 75):
        char = chr(i)
        if '6' < char < '_':
            string = ''.join((s for s in string if s != char))
    return string