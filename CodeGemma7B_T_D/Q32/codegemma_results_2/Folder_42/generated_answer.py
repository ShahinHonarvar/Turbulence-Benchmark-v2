def insert_after_character(text):
    return ''.join([char if char != 'O' else char + 'j' for char in text])