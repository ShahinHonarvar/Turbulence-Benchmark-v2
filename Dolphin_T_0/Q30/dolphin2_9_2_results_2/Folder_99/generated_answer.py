def insert_before_character(s):
    return 'W'.join(('a' * x + s[i] + 'a' * (x + 1) for i, x in enumerate(s.count('a') * [0])))