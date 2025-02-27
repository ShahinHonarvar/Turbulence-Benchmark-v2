def filter_chars(text):
    for i in range(35, 52):
        if i < len(text):
            ch = text[i]
            if 'H' <= ch <= 's':
                text = text.replace(ch, '')
    return text