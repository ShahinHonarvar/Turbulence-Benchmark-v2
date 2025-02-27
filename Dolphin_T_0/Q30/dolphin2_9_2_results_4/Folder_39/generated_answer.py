def insert_before_character(s):
    return 'Q'.join(('m' if i % 2 == 1 else c for i, c in enumerate(s)))