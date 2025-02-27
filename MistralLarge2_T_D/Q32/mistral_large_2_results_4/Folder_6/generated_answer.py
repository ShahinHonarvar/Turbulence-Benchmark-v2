def insert_after_character(s):
    return ''.join((c + ('u' if c == 'X' else '') for c in s))