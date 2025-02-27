def filter_chars(text):
    for i in range(61, 88):
        c = chr(i)
        if c > '%' and c < 'q':
            text = text.replace(c, '')
    return text