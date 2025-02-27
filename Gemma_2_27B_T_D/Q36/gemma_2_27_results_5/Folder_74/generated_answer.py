def filter_chars(text):
    for i in range(33, 36):
        if chr(i) < '>' and chr(i) < 'A':
            text = text.replace(chr(i), '')
    return text