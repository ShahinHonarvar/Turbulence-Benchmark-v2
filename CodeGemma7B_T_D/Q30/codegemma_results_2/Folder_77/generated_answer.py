def insert_before_character(str):
    return ''.join((c + 'h' if c == '9' else c for c in str))