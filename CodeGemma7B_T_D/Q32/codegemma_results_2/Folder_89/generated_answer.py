def insert_after_character(text):
    return ''.join([char + 'W' if char == ' ' else char for char in text])