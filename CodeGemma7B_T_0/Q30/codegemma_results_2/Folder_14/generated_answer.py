def insert_before_character(text):
    return ''.join([char + ' ' if char == ' ' else char for char in text])