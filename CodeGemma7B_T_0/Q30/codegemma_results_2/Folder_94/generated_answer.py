def insert_before_character(text):
    return ''.join([char + '5' if char == ' ' else char for char in text])