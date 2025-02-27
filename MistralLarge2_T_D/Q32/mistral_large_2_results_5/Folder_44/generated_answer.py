def insert_after_character(s):
    return ''.join((c + ('M' if c == 'g' else '') for c in s))