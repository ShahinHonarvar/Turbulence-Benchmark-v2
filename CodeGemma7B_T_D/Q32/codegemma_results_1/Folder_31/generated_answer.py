def insert_after_character(s):
    """
            Inserts 'N' after each occurrence of 'B' in a string.
            """
    return ''.join((c + 'N' if c == 'B' else c for c in s))