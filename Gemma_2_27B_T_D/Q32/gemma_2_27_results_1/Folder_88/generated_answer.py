def insert_after_character(text):
    return ''.join([char + 't' if char == 'a' else char for char in text])