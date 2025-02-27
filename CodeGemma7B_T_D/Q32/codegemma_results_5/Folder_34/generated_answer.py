def insert_after_character(string):
    return ''.join([c for c in string if c != 'A'] + ['a'] + [c for c in string if c == 'A'])