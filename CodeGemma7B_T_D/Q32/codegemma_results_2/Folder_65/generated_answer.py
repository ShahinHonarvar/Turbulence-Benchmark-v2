def insert_after_character(text):
    return ''.join([char + '9' if char == '6' else char for char in text])