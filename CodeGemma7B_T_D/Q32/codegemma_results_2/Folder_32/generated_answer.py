def insert_after_character(str):
    return ''.join((c + 'u' if c == 'F' else c for c in str))