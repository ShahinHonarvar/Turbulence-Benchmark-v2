def insert_after_character(s):
    return ''.join(('H' if p == 'A' else p for p in s)) + 'H'