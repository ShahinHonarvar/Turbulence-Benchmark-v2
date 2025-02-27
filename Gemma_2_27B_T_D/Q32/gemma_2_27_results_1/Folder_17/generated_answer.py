def insert_after_character(text):
    return ''.join(['I' + c if c == 'Q' else c for c in text])