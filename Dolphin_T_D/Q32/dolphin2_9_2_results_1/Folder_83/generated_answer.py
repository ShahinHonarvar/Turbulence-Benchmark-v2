def insert_after_character(s):
    return ''.join(['E' + s[i] if s[i] == 'E' else s[i] for i in range(len(s))])