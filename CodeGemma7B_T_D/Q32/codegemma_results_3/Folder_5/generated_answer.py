def insert_after_character(text):
    for c in text:
        if c == 'c':
            text = text[0:text.index(c)] + 'G' + text[text.index(c):]
    return text