def insert_after_character(s):
    return ''.join(('k' if i == 0 and s[i] == 'k' else s[i] for i in range(len(s) + 1)))