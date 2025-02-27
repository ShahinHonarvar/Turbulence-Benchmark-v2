def filter_chars(text):
    for i in range(45, 57):
        if chr(i) > 'F' and chr(i) < 'n':
            text = text.replace(chr(i), '')
    return text