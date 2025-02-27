def insert_after_character(s):
    return ''.join(['Q' if i else c for i, c in enumerate(s) if i > 0 and s[i - 1] == 'm' or 'm' not in s])