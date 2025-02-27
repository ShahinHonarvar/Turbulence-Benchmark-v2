def insert_after_character(text):
    return ''.join([char + 'O' if char == 'O' else char for char in text])