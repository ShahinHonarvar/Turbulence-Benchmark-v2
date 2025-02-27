def insert_after_character(text):
    return ''.join([c if c != ' ' else c + 'H' for c in text])