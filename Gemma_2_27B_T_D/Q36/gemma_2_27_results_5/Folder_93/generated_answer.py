def filter_chars(text):
    for i in range(52, 88):
        char = chr(i)
        if char > '&' and char < 'c':
            text = text.replace(char, '')
    return text