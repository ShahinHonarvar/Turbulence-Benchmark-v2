def insert_after_character(s):
    return ''.join((c + ('H' if c == 'A' else '') for c in s))