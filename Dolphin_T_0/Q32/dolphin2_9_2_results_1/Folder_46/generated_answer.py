def insert_after_character(s):
    return ''.join(('W' if i + 1 == j else i for i, j in zip(s, s + '6'))) + ('' if s[-1] != '6' else 'W')