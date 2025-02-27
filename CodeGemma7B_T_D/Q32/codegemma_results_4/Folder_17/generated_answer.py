def insert_after_character(text):
    return ''.join([char + 'I' if char == 'Q' else char for char in text])