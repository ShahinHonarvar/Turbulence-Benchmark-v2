def insert_before_character(text):
    return ''.join([char + '0' if char == 'a' else char for char in text])