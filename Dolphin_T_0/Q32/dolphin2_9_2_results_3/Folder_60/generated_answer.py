def insert_after_character(s):
    return ''.join(('C' + 'P' if i > 0 and s[i - 1] == 'C' else s[i] for i, c in enumerate(s)))