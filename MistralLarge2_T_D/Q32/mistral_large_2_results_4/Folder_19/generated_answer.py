def insert_after_character(s):
    return ''.join((c + ('h' if c == '5' else '') for c in s))