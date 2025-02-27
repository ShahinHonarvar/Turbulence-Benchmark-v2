def insert_after_character(text):
    """Inserts 'P' immediately succeeding 'C' in text."""
    return ''.join((c + 'P' if c == 'C' else c for c in text))