def insert_after_character(text: str) -> str:
    """Inserts 's' immediately succeeding any occurrences of 'H' in a string."""
    return ''.join([ch + ('s' if ch == 'H' else '') for ch in text])