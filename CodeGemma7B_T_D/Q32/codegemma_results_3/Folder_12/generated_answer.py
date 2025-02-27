def insert_after_character(text):
    return ''.join([char + ' ' if char == 'I' else char for char in text])