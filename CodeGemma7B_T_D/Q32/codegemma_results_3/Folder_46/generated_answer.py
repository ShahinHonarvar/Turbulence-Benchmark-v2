def insert_after_character(text):
    return ''.join((c + 'W' if c == '6' else c for c in text))