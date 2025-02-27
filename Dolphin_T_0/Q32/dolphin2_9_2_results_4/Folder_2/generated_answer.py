def insert_after_character(string):
    return ''.join(('Z' if i > 0 and string[i - 1] == 'C' else c for i, c in enumerate(string)))