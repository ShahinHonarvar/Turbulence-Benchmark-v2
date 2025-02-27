def insert_after_character(s):
    return ''.join((c + ('A' if c == 'a' else '') for c in s))