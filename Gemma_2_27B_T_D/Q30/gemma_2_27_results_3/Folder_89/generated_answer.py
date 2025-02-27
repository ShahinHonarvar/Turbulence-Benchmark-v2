def insert_before_character(text):
    return ''.join(['W' + c if c == ' ' else c for c in text])