def filter_chars(text):
    for i in range(51, 76):
        c = chr(i)
        if c > '5' and c < 'f':
            text = text.replace(c, '')
    return text