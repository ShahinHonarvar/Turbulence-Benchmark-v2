def insert_after_character(s):
    return ''.join(('0H' if c == '0' else c for c in s))