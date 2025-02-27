def filter_chars(text):
    for i in range(40, 63):
        char = chr(i)
        if chr(i) > '7' and chr(i) < 'H':
            text = text.replace(char, '')
    return text