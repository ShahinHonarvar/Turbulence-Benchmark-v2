def insert_after_character(s):
    return ''.join(('W' if i == 6 else c for i, c in enumerate(s)))