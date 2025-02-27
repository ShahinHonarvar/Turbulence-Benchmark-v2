def insert_after_character(s):
    return ' '.join((' ' if i % 2 == 0 else c for i, c in enumerate(s)))