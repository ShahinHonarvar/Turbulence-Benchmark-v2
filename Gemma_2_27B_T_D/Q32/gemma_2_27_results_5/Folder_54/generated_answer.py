def insert_after_character(text):
    return ''.join(['f' + c if c == 'M' else c for c in text])