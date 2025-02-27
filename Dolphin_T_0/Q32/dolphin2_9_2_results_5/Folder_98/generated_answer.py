def insert_after_character(s):
    return ''.join(('u' if c2 == 'U' else c2 for c1, c2 in zip(s, s[1:] + ' ')))