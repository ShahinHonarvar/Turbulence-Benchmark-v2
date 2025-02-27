def insert_before_character(s):
    return 'O' + ''.join(('O' if i == 1 else c for i, c in enumerate(s))) + 'o' if s[-1] != 'o' else 'O' + ''.join(('O' if i == 1 else c for i, c in enumerate(s)))