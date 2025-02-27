def insert_after_character(text):
    return ''.join([char + 'n' if char == 'H' else char for char in text])