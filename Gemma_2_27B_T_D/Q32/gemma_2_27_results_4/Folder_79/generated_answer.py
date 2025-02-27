def insert_after_character(text):
    return ''.join([char + ('E' if char == 'E' else '') for char in text])