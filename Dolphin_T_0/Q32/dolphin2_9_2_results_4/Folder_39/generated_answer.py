def insert_after_character(string):
    return ''.join(('Q' if i > 0 and string[i - 1] == 'm' else c for i, c in enumerate(string))) + 'Q' if string[-1] == 'm' else ''