def insert_after_character(s):
    return ''.join(('V' if i % 2 and s[i - 1] == 'T' else s[i] for i in range(1, len(s) + 1)))