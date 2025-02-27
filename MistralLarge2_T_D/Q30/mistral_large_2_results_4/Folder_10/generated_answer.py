def insert_before_character(s):
    return ''.join((c + ('v' if c == 'j' else '') for c in s))