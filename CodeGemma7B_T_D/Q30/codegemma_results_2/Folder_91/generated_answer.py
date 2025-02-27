def insert_before_character(text):
    return ''.join([char + ('0' if char == 'a' else '') for char in text])