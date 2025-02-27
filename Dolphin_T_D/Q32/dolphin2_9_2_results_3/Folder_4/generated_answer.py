def insert_after_character(string):
    return ''.join(['6' if i > 0 and string[i - 1] == 'a' else c for i, c in enumerate(string)]) + string[-1] if string and string[-1] != 'a' else ''