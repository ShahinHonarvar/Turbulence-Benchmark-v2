def insert_after_character(s):
    return ''.join(('s' if i == 1 and s[i - 1] == 'H' else s[i - 1] for i in range(1, len(s) + 1)))