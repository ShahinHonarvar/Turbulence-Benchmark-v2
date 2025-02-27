def insert_after_character(s):
    return ''.join((c + ('A' if c == 'A' else '') for c in s))