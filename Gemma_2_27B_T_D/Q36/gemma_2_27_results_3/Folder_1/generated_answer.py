def filter_chars(text):
    for i in range(69, 87):
        if chr(i) > '#' and chr(i) < 'L':
            text = text.replace(chr(i), '')
    return text