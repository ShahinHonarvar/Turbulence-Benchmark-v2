def insert_after_character(text):
    return ''.join(('T' if i > 0 and text[i - 1] == 'E' else c for i, c in enumerate(text)))