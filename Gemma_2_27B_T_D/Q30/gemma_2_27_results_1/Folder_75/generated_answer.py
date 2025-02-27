def insert_before_character(text):
    return ''.join(['q' + c if c == 'U' else c for c in text])