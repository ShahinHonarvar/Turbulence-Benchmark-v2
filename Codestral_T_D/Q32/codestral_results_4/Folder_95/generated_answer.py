def insert_after_character(s):
    return ''.join(('q' if c == 'j' else c for c in s)) + 'q' if s[-1] == 'j' else s