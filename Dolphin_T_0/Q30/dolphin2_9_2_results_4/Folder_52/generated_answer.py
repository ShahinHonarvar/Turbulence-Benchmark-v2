def insert_before_character(s):
    return 'V'.join(('T' if c == 'T' else c for c in s)) + 'T'[s[-1] == 'T']