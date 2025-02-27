def insert_before_character(s):
    return ''.join(('q' if i + 1 == j else s[j] for j, i in enumerate(s)))