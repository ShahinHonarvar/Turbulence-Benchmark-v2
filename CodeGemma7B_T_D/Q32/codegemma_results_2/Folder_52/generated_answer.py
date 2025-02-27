def insert_after_character(text):
    return ''.join([char + 'V' if char == 'T' else char for char in text])