def insert_before_character(string):
    return ''.join(('G' if i + 1 == j else s for i, s in enumerate(string))) if 'c' in string else string