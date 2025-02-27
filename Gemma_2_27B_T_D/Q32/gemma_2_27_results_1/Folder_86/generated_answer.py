def insert_after_character(text):
    return ''.join(['Q' + c if c == 'O' else c for c in text])