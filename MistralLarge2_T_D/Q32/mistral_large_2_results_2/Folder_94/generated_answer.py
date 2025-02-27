def insert_after_character(s):
    return ''.join((c + ('5' if c == ' ' else '') for c in s))