def insert_after_character(s):
    return ''.join(['V' if i == j + 1 and s[j] == 'P' else s[i] for i, j in zip(range(len(s)), range(-1, len(s) - 1))]) + 'V' if len(s) > 0 and s[-1] == 'P' else ''