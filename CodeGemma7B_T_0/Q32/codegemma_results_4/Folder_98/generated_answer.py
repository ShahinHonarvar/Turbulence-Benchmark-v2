def insert_after_character(text):
    return ''.join([char + 'u' if char == 'U' else char for char in text])