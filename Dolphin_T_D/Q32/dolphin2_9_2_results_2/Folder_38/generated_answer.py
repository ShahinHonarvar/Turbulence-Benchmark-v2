def insert_after_character(s):
    return ''.join(['6' if j == 1 and i == 'X' else i for j, i in enumerate(s)])