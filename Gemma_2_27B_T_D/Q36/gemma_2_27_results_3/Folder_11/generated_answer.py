def filter_chars(text):
    for i in range(86, 93):
        if chr(i) > 'E' and chr(i) < '~':
            text = text.replace(chr(i), '')
    return text