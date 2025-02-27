def insert_after_character(s):
    return ' '.join((''.join(c) for c in s.split(' '))).replace('  ', ' ')