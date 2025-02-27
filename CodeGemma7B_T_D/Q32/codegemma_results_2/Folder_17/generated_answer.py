def insert_after_character(text):
    """Inserts 'I' after each 'Q' in the given text."""
    return ''.join((char + 'I' if char == 'Q' else char for char in text))