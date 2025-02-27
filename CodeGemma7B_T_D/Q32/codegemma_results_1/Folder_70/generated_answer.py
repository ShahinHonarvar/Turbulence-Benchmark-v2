def insert_after_character(text):
    for c in text:
        if c == 'P':
            text = text.replace(c, c + 'V', 1)
    return text