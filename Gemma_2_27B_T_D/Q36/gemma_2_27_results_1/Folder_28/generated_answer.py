def filter_chars(text):
    for i in range(31, 73):
        if chr(i) > 'M' and chr(i) < 'j':
            text = text.replace(chr(i), '')
    return text