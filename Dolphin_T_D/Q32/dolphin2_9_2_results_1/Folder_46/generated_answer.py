def insert_after_character(s):
    return ''.join(('W' if i > 0 and s[i - 1] == '6' else char for i, char in enumerate(s))) + ('' if s and s[-1] != '6' else 'W')