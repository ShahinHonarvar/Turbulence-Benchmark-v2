def insert_after_character(text):
    return ''.join([char + 'P' if char == ' ' else char for char in text])