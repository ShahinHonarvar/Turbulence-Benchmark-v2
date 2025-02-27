def insert_after_character(string):
    return ''.join(('U' if a == 'U' and i != 0 and (string[i - 1] != 'U') else a for i, a in enumerate(string)))