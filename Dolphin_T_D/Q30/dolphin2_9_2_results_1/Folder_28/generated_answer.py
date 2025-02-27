def insert_before_character(s):
    return ''.join(('1' + s[i] if s[i] == 'r' else s[i] for i in range(len(s) - 1))) + ('' if s[-1] != 'r' else '1' + s[-1])