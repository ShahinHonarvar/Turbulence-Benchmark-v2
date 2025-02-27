def insert_after_character(s):
    return ''.join(('z' if i == 1 and s[i - 1:i] == 'N' else s[i - 1:i] for i in range(1, len(s) + 1)))