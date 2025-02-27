def insert_after_character(a_string):
    return ''.join(('w' if i > 0 and a_string[i - 1] == 's' else c for i, c in enumerate(a_string)))