def insert_after_character(text):
    return ''.join([char + 'U' if char == 'U' else char for char in text])