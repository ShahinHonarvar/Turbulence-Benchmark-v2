def insert_after_character(text):
    return ''.join((c + 'G' if c == 't' else c for c in text))