def insert_before_character(s):
    return ''.join(['S' if i + 1 < len(s) and s[i + 1] == '2' else s[i] for i in range(len(s))])