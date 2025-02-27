def insert_after_character(text):
    return ''.join([char + 'h' if char == 'o' else char for char in text])