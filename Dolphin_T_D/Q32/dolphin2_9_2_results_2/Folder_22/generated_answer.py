def insert_after_character(string):
    return ''.join(('U' if i > 0 and string[i - 1] == 'U' else char for i, char in enumerate(string))) + 'U' if string else ''