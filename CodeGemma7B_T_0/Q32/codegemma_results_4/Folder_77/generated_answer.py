def insert_after_character(text):
    return ''.join([char + 'h' if char == '9' else char for char in text])