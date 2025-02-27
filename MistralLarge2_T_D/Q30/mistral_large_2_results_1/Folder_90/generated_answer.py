def insert_before_character(s):
    return ''.join((c + ('F' if c == 'U' else '') for c in s))