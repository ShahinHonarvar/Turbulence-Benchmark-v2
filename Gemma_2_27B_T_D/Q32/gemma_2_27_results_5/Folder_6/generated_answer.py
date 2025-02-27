def insert_after_character(text):
    return ''.join(['u' + c if c == 'X' else c for c in text])