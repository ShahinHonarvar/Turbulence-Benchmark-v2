def insert_before_character(string):
    return 'a'.join((c + 'U' if c == 'U' else c for c in string))