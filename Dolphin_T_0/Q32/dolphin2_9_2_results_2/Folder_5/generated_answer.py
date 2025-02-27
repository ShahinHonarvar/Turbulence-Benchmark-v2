def insert_after_character(s):
    return ''.join(['G' if i != 0 and s[i - 1] == 'c' else s[i] for i in range(len(s))])