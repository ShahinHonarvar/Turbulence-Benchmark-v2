def insert_before_character(text):
    return ''.join([char + 'k' if char == 'k' else char for char in text])