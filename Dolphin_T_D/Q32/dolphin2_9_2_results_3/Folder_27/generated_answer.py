def insert_after_character(s):
    return ''.join(('j' if i + 1 == s.find('N', i + 1) else c for i, c in enumerate(s)))