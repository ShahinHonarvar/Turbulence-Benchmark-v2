def insert_after_character(text):
    """Inserts 'e' after every occurrence of 'E' in the input string."""
    return ''.join([char + ('e' if char == 'E' else '') for char in text])