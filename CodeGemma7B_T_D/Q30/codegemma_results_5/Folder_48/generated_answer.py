def insert_before_character(text):
    return ''.join([char for char in text if char != 'S'] + ['U' if char == 'S' else char for char in text])