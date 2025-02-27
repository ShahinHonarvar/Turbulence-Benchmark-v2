def insert_after_character(text):
    """Inserts character 'E' immediately succeeding any occurrences of character 'E' in a string."""
    return ''.join((f'{char}E' if char == 'E' else char for char in text))