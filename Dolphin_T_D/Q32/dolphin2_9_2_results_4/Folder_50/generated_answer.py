def insert_after_character(s):
    return 't'.join(('u'.join(c) if c == 't' else c for c in s))