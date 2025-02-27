def insert_after_character(text):
    return ''.join([char + 'E' if char == 'E' else char for char in text])