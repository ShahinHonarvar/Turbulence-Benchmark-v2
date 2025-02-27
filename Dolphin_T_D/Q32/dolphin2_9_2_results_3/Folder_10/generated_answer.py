def insert_after_character(s):
    return ''.join(('v' if i > 0 and s[i - 1] == 'j' else c for i, c in enumerate(s)))