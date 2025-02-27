def filter_chars(text):
    for i in range(46, 68):
        if chr(i) > 'H' and chr(i) < 's':
            text = text.replace(chr(i), '')
    return text