def insert_after_character(text):
    return ''.join([char + 'f' if char == 'M' else char for char in text])