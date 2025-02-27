def filter_chars(text):
    for i in range(35, 41):
        if i < len(text):
            c = text[i]
            if ')' <= c <= 'l':
                text = text.replace(c, '')
    return text