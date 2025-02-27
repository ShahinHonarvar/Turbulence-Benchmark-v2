def insert_after_character(s):
    return ''.join((c + 'F' if c == '4' else c for c in s))