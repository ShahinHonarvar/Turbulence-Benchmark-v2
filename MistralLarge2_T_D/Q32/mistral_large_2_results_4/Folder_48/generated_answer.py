def insert_after_character(s):
    return ''.join((c + ('U' if c == 'S' else '') for c in s))