def insert_after_character(text):
    return ''.join([char for char in text if char != 'w'] + ['n' if char == 'w' else char for char in text])