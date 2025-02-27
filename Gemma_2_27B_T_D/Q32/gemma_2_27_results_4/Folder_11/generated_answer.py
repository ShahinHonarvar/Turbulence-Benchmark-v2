def insert_after_character(text):
    return ''.join((c + 't' if c == 'g' else c for c in text))