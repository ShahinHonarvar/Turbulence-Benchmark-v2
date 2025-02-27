def insert_before_character(text):
    return ''.join([char + 'A' if char == 'a' else char for char in text])