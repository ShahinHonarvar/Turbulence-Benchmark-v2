def insert_after_character(text):
    return ''.join(['9' + c if c == '6' else c for c in text])