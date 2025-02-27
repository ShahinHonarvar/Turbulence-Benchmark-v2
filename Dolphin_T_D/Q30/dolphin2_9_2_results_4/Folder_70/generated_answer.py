def insert_before_character(s):
    return ''.join(['V' if i + 1 < len(s) and s[i + 1] == 'P' else char for i, char in enumerate(s)]) + ('' if s[-1] != 'P' else 'V')