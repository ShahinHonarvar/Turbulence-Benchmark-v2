def filter_chars(text):
    for i in range(46, 68):
        char = text[i]
        if 'H' < char < 's':
            text = text.replace(char, '')
    return text