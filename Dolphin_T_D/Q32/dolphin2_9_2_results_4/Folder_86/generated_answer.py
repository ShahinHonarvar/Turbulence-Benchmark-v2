def insert_after_character(s):
    return ''.join(('Q' if i + 1 == j else s[j] for i, j in enumerate(s.replace('O', 'OQ'))))