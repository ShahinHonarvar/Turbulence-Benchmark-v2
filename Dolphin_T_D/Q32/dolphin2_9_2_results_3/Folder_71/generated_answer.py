def insert_after_character(string):
    return ''.join(('S' if (index, char) == (i, '2') else char for i, char in enumerate(string)))