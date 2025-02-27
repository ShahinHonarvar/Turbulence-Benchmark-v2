def insert_before_character(text):
    return ''.join([char + 'E' if char == 'e' else char for char in text])