def insert_after_character(s):
    return ''.join(['n' if i < len(s) and s[i] == 'H' and (s[i - 1] != 'H') else s[i] for i in range(len(s) + 1)])