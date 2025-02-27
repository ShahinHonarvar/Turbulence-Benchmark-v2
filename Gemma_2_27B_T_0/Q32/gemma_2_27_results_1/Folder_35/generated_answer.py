def insert_after_character(text):
    return ''.join(['M' + c if c == '9' else c for c in text])