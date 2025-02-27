def insert_before_character(text):
    return ''.join(['0' + c if c == 'e' else c for c in text])