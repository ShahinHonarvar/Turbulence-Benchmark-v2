def insert_after_character(s):
    return ''.join(['A' if i > 0 and s[i] == 'a' and (s[i - 1] != 'a') else s[i] for i in range(len(s))])