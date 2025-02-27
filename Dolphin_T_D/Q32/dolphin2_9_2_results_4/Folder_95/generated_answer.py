def insert_after_character(text):
    return ''.join(('q' if character == 'j' else character for character in text))