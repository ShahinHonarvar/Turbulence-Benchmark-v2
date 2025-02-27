def insert_after_character(s):
    return ''.join(['h' if i == 1 and c == '9' else c for i, c in enumerate(s)])