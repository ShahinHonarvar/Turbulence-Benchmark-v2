def insert_before_character(text):
    return ''.join(['N' + c if c == 'm' else c for c in text])