def insert_before_character(s):
    return ''.join(['Q' if s[i - 1] == 'O' else s[i] for i in range(len(s))])