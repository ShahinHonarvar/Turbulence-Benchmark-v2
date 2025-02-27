def insert_before_character(text):
    return ''.join([char + ('o' if char == 'F' else '') for char in text])