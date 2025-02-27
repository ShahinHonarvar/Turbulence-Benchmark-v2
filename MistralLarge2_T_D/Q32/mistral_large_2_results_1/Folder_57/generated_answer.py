def insert_after_character(s):
    return ''.join((c + ('w' if c == 's' else '') for c in s))