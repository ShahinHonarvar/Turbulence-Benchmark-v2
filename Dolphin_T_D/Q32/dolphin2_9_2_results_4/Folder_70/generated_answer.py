def insert_after_character(s):
    return ''.join(('V' if i > 0 and s[i - 1] == 'P' else s[i] for i in range(len(s)))) + ('' if s[-1] != 'P' else 'V')