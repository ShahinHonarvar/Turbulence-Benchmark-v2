def insert_before_character(s):
    return 'o'.join(('F' if c == 'F' else 'o' if p == 'F' else c for p, c in zip(' ' + s, s)))