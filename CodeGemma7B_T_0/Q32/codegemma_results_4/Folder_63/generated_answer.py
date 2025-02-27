def insert_after_character(text):
    return ''.join([char + 'R' if char == '5' else char for char in text])