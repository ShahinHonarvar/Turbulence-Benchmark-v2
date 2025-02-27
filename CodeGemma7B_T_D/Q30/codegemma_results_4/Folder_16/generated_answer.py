def insert_before_character(text):
    return ''.join([char + 'n' if char == 'w' else char for char in text])