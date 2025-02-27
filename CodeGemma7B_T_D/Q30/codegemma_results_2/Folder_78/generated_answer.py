def insert_before_character(text):
    return ''.join([char if char != 'H' else char + 's' for char in text])