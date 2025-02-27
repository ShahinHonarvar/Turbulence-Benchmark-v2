def insert_after_character(s):
    return ' '.join((''.join((c if c != ' ' else 'H ' for c in s)) for s in s.split()))