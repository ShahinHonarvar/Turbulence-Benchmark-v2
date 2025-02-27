def filter_chars(text):
    for i in range(55, 66):
        if chr(i) > 'f' and chr(i) < '|':
            text = text.replace(chr(i), '')
    return text