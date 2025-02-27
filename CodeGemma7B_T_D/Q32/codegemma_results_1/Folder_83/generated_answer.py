def insert_after_character(text):
    """Inserts 'e' immediately succeeding any occurrences of 'E' in a string."""
    return ''.join((c + 'e' if c == 'E' else c for c in text))