def insert_after_character(s):
    return ''.join((c + ('G' if c == 'c' else '') for c in s))