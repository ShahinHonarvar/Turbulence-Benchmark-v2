def filter_chars(text):
    for i in range(55, 80):
        if chr(i) > 'S' and chr(i) < 's':
            text = text.replace(chr(i), '')
    return text