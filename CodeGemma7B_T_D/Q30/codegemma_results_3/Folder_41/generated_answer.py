def insert_before_character(text):
    return ''.join([char + ('o' if char == 'O' else '') for char in text])