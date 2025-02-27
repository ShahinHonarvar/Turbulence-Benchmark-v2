def filter_chars(text):
    for i in range(46, 68):
        c = text[i]
        if c > 'H' and c < 's':
            text = text.replace(c, '')
    return text