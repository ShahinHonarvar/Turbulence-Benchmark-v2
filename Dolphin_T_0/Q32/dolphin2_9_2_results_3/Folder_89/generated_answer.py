def insert_after_character(s):
    return ' '.join((c for c in s if c != ' ')) + 'W' * s.count(' ')