def insert_before_character(text):
    for i, c in enumerate(text):
        if c == 'r':
            return text[:i] + '1' + text[i:]
    return text