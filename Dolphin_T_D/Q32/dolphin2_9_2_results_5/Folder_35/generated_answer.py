def insert_after_character(s):
    return ''.join(['M' if i + 1 < len(s) and s[i] == '9' and (s[i + 1] != 'M') else s[i] for i in range(len(s))]) + ('' if s[-1] != '9' else 'M')