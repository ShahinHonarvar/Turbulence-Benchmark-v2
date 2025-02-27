def insert_before_character(text):
    return ''.join([char + 'I' if char == 'i' else char for char in text])