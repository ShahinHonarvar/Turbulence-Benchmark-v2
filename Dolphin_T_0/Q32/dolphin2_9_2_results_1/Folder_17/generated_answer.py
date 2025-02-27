def insert_after_character(s):
    return ''.join(('I' if c == 'Q' else c for c in s)) + 'I' if s[-1] == 'Q' else ''