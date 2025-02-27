def insert_after_character(text):
    return ''.join([char + 'N' if char == 'B' else char for char in text])