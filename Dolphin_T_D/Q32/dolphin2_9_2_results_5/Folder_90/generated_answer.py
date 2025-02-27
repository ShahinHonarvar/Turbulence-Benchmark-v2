def insert_after_character(string):
    return ''.join(('F' if i > 0 and string[i - 1] == 'U' else ch for i, ch in enumerate(string))) + 'F' if string and string[-1] == 'U' else ''