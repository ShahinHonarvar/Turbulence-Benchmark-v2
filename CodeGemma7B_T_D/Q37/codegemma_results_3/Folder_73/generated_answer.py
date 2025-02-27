def filter_chars(text):
    out = ''
    for i, char in enumerate(text):
        if not (i >= 22 and i <= 85 and (char >= '7') and (char <= 'e')):
            out += char
    return out