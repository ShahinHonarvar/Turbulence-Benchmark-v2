def insert_after_character(s):
    return ''.join(('M' if c == 'g' else c for c in s)) + (s[-1] != 'g' and 'M' or '')