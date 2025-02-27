def insert_after_character(text):
    return ''.join([char + 'o' if char == 'o' else char for char in text])