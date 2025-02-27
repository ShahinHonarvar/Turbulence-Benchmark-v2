def insert_after_character(text):
    return ''.join((char + ('e' if char == 'E' else '') for char in text))