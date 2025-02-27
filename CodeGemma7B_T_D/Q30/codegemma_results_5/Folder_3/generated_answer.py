def insert_before_character(text):
    return ''.join((c + 'H' if c == '0' else c for c in text))