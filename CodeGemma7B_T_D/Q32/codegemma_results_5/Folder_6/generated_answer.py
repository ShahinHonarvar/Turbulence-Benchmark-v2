def insert_after_character(text):
    return ''.join((char + 'u' if char == 'X' else char for char in text))