def insert_after_character(text):
    return ''.join(['X' + c if c == ' ' else c for c in text])