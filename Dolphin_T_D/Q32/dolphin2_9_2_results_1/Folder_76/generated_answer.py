def insert_after_character(s):
    return ''.join(['m' if i > 1 and s[i - 1] == 'F' else s[i] for i in range(len(s))])