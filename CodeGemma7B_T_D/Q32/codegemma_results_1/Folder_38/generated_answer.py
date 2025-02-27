def insert_after_character(text):
    return ''.join([char for char in text if char != 'X'] + ['6' if char == 'X' else char for char in text])