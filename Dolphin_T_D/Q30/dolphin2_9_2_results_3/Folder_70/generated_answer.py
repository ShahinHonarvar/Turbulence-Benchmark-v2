def insert_before_character(s):
    return ''.join(('V' if i + 1 == j else s[j] for j, i in enumerate(s) if s[j] in 'Pp'))