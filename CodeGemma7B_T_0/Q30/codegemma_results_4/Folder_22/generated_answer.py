def insert_before_character(text):
    return ''.join([char + 'U' if char == 'U' else char for char in text])