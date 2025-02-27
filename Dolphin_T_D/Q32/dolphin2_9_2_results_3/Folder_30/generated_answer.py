def insert_after_character(s):
    return ''.join(('F' if i > 0 and s[i - 1] == '4' else ch for i, ch in enumerate(s))) + 'F' if s[-1] == '4' else ''