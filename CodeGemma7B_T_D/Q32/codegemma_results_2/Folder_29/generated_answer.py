def insert_after_character(text):
    return ''.join((char + 'z' if char == 'N' else char for char in text))