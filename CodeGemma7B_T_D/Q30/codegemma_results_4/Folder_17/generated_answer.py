def insert_before_character(text):
    return ''.join([char if char != 'Q' else 'I' + char for char in text])