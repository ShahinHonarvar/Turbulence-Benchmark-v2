def insert_before_character(s):
    return ''.join(['l' if i == 'K' or (j == 'K' and j != len(s) - 1) else s[j] for i, j in enumerate(s)])