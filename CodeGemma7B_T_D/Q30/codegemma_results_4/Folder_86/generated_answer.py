def insert_before_character(text):
    return ''.join([char if char != 'O' else 'Q' + char for char in text])