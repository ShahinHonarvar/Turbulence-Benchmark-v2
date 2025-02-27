def insert_after_character(s):
    return ' '.join(('o' if i == 1 and c == ' ' else c for i, c in enumerate(s)))