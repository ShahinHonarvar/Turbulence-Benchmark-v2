def insert_after_character(s):
    """Inserts 'a' immediately succeeding any occurrences of 'U' in a string."""
    return ''.join([i + 'a' if i == 'U' else i for i in s])