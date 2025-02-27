def insert_after_character(s):
    return ''.join((c + ('u' if c == 'F' else '') for c in s))