def filter_chars(text):
    for i in range(46, 74):
        if chr(i) > '&' and chr(i) < 'M':
            text = text.replace(chr(i), '')
    return text