def insert_before_character(text):
    return ''.join([char for char in text if char != 'h'] + ['h'] + [char for char in text if char == '5'])