def insert_after_character(s):
    return ''.join(['S' if i == 2 else j for i, j in enumerate(s)])