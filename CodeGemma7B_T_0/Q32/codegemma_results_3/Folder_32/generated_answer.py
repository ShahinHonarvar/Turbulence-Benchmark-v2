def insert_after_character(text):
    return ''.join([char + 'u' if char == 'F' else char for char in text])