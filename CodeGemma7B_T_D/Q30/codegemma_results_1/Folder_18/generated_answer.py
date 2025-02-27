def insert_before_character(text):
    return ''.join([char + 'l' if char == 'K' else char for char in text])