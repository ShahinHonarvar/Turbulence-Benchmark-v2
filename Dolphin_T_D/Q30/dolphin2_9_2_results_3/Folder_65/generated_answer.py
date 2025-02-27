def insert_before_character(s):
    return ''.join(('9' if i + 1 == s.index('6') else j for i, j in enumerate(s)))