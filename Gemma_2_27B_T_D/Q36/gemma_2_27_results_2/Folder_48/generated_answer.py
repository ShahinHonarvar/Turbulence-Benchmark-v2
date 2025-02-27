def filter_chars(text):
    for i in range(154, 222):
        if chr(i) > 'A' and chr(i) < 'f':
            text = text.replace(chr(i), '')
    return text