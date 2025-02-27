def insert_after_character(text):
    """Inserts a character immediately succeeding any occurrences of another character in a string."""
    return ''.join([char + 'a' if char == 'o' else char for char in text])