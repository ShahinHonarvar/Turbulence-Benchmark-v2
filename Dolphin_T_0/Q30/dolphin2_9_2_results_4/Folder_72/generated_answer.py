def insert_before_character(s):
    return ''.join(['d' if i == len(s) - 1 or s[i] != 'O' else 'dO' + s[i + 1:] for i in range(len(s))])