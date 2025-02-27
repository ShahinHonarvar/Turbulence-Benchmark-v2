def insert_after_character(text):
    """Inserts '9' immediately succeeding any occurrences of '6' in a string."""
    return ''.join([char + ('9' if char == '6' else '') for char in text])