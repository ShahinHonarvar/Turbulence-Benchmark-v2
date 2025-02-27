def insert_before_character(text):
    return ''.join([char + 'a' if char == 'a' else char for char in text])