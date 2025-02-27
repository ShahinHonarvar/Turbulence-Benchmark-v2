def insert_before_character(text):
    return ''.join([char for char in text if char != 'o'] + ['a' if char == 'o' else char for char in text])