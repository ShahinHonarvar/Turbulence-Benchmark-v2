def filter_chars(text):
    out = ''
    for idx, char in enumerate(text):
        if idx >= 8 and idx <= 9 and (char >= 'R') and (char <= 't'):
            continue
        out += char
    return out