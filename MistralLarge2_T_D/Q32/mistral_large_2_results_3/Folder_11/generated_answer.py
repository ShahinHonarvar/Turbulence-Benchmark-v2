def insert_after_character(s):
    return ''.join((c + ('t' if c == 'g' else '') for c in s))