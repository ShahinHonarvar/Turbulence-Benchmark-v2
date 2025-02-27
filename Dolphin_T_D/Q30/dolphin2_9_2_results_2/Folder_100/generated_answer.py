def insert_before_character(s):
    return ' '.join(('0' if c == '0' else str(c) for c in s))