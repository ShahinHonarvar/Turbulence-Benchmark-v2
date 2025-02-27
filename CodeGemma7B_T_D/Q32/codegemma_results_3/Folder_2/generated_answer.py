def insert_after_character(text):
    return ''.join((char + 'Z' if char == 'C' else char for char in text))