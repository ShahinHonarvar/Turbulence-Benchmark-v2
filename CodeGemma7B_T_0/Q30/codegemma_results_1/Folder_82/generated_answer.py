def insert_before_character(text):
    return ''.join([char + 'I' if char == 'I' else char for char in text])