def insert_before_character(text):
    return ''.join([char + 'o' if char == 'o' else char for char in text])