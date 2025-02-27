def insert_before_character(text):
    return ''.join([char + ('u' if char == 'u' else '') for char in text])