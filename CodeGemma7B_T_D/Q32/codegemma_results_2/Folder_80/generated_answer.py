def insert_after_character(text):
    return ''.join([char + 'X' if char == ' ' else char for char in text])