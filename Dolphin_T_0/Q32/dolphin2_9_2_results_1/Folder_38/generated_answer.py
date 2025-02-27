def insert_after_character(s):
    return ''.join(['6' if s[i:i + 2] == 'X6' else s[i] for i in range(len(s))])