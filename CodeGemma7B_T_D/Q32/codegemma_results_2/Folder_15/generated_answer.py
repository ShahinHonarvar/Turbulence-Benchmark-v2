def insert_after_character(text):
    """Inserts 'o' after character 'o' in a string."""
    return ''.join((char + 'o' if char == 'o' else char for char in text))