def insert_after_character(text):
    return ''.join(['T' + c if c == 'U' else c for c in text])