def insert_before_character(text):
    return ''.join((char + 'i' if char == 'i' else char for char in text))