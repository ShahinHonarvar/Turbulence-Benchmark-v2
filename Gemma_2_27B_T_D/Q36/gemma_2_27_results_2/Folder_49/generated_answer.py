def filter_chars(text):
    for i in range(46, 91):
        char = chr(i)
        if char > 'D' and char < 'H':
            text = text.replace(char, '')
    return text