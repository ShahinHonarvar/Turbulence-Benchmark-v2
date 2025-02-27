def insert_after_character(text):
    return ''.join([char if char != 'U' else char + 'T' for char in text])