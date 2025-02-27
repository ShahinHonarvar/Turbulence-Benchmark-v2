def insert_after_character(s):
    return ''.join(['a' if i > 0 and s[i - 1] == 'o' else s[i] for i in range(len(s))])