def insert_after_character(text):
    return ''.join((char if char != 'F' else 'Fm' if idx < len(text) - 1 else 'F' for idx, char in enumerate(text)))