def insert_after_character(s):
    return ''.join(('w' if i > 0 and s[i - 1] == 's' else s[i] for i in range(len(s)))) + ('' if s[-1] != 's' else 'w')