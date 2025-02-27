def insert_after_character(s):
    return ''.join(['0' if i + 1 < len(s) and s[i] == 'o' and (s[i + 1] != '0') else s[i] + ('' if i + 1 == len(s) or s[i + 1] != '0' else '0') for i in range(len(s))])