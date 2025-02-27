def insert_after_character(s):
    return ''.join([s[i] if s[i] != 'g' else 'gt' if i != len(s) - 1 else 'g' for i in range(len(s))])