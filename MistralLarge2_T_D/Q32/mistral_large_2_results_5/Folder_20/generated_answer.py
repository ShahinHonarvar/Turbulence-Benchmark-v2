def insert_after_character(s):
    return ''.join((c + ('H' if c == 'C' else '') for c in s))