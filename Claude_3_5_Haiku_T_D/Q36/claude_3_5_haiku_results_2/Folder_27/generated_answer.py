def filter_chars(s):
    result = list(s)
    for i in range(49, 75):
        char = chr(i)
        if '6' < char < '_':
            result = [c for c in result if c != char]
    return ''.join(result)