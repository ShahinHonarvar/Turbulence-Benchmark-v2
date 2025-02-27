def insert_before_character(text):
    """Inserts 'v' before every 'j' in a string."""
    return ''.join([char if char != 'j' else 'v' + char for char in text])