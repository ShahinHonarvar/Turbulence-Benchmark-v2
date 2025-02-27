def insert_after_character(s):
    return ''.join(['n' if i > 0 and s[i - 1] == 'w' else s[i] if s[i] != 'w' else s[i] + 'n' for i in range(len(s))])