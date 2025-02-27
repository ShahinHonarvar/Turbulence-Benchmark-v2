def filter_chars(text):
    filtered = ''
    for i in range(len(text)):
        if i >= 38 and i <= 99 and (text[i].upper() >= 'A') and (text[i].upper() <= 'Q'):
            continue
        else:
            filtered += text[i]
    return filtered