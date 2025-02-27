def filter_chars(text):
    for i in range(46, 68):
        char = text[i]
        if char > 'H' and char < 's':
            text = text.replace(char, '')
    return text