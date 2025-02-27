def insert_after_character(s):
    return ''.join(['n' if i > 0 and s[i - 1] == 'a' and (s[i] != 'n') else s[i] for i in range(len(s))])