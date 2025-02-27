def insert_after_character(text):
    return ''.join((character + 'P' if character == 'C' else character for character in text))