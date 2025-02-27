def insert_after_character(string):
    return ''.join(['a' if c == 'a' else '' for c in string] + list(string))