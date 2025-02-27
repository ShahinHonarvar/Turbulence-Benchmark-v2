def insert_after_character(s):
    return ''.join(('0' if y == 'i' else y for x, y in enumerate(s))) + ('' if s[-1] != 'i' else '0')