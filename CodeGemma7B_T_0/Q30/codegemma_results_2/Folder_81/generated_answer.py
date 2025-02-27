def insert_before_character(text):
    return ''.join([char + 'A' if char == 'A' else char for char in text])